#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import time
from pathlib import Path

try:
    from fetch_dylan_patel_transcripts import VIDEOS, write_outputs
except ModuleNotFoundError:
    from scripts.fetch_dylan_patel_transcripts import VIDEOS, write_outputs
from openai import OpenAI


TERMS_PROMPT = (
    "This is an interview with Dylan Patel, founder of SemiAnalysis. "
    "Technical terms may include SemiAnalysis, Nvidia, CUDA, GPU, TPU, HBM, DRAM, "
    "TSMC, ASML, Applied Materials, Lam Research, hyperscalers, AI labs, data centers, "
    "semiconductors, foundries, China export controls, inference, training, and capex."
)


def run(command):
    subprocess.run(command, check=True)


def duration_seconds(path):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    return float(result.stdout.strip())


def ensure_chunks(audio_path, chunk_dir, segment_time):
    chunk_dir.mkdir(parents=True, exist_ok=True)
    chunks = sorted(chunk_dir.glob("chunk_*.mp3"))
    if chunks:
        return chunks

    run(
        [
            "ffmpeg",
            "-hide_banner",
            "-y",
            "-i",
            str(audio_path),
            "-ac",
            "1",
            "-ar",
            "16000",
            "-b:a",
            "48k",
            "-f",
            "segment",
            "-segment_time",
            str(segment_time),
            "-reset_timestamps",
            "1",
            str(chunk_dir / "chunk_%03d.mp3"),
        ]
    )
    return sorted(chunk_dir.glob("chunk_*.mp3"))


def as_dict(response):
    if hasattr(response, "model_dump"):
        return response.model_dump()
    if isinstance(response, dict):
        return response
    return json.loads(response.model_dump_json())


def transcribe_chunk(client, chunk_path, model, cache_path, prompt):
    if cache_path.exists():
        return json.loads(cache_path.read_text())

    with chunk_path.open("rb") as audio:
        for attempt in range(5):
            try:
                request = {
                    "model": model,
                    "file": audio,
                    "language": "en",
                    "response_format": "verbose_json",
                    "temperature": 0,
                }
                if prompt:
                    request["prompt"] = prompt
                response = client.audio.transcriptions.create(**request)
                payload = as_dict(response)
                cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
                return payload
            except Exception:
                if attempt == 4:
                    raise
                audio.seek(0)
                time.sleep(2 * (attempt + 1))


def normalize_segments(payload, offset, fallback_duration):
    segments = payload.get("segments") or []
    normalized = []
    for segment in segments:
        text = " ".join((segment.get("text") or "").split())
        if not text:
            continue
        start = float(segment.get("start", 0) or 0)
        end = float(segment.get("end", start) or start)
        normalized.append(
            {
                "text": text,
                "start": round(offset + start, 3),
                "duration": round(max(0.0, end - start), 3),
            }
        )
    if normalized:
        return normalized

    text = " ".join((payload.get("text") or "").split())
    if not text:
        return []
    return [{"text": text, "start": round(offset, 3), "duration": round(fallback_duration, 3)}]


def find_video(video_id):
    for video in VIDEOS:
        if video["id"] == video_id:
            return video
    raise ValueError(f"unknown video id: {video_id}")


def drop_trailing_artifacts(transcript):
    while transcript:
        last = transcript[-1]
        text = (last.get("text") or "").strip().lower()
        duration = float(last.get("duration", 0) or 0)
        if text in {"you"} and duration <= 2:
            transcript.pop()
            continue
        break
    return transcript


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True, type=Path)
    parser.add_argument("--video-id", required=True)
    parser.add_argument("--chunk-dir", type=Path, default=Path("/tmp/dylan-audio-chunks"))
    parser.add_argument("--segment-time", type=int, default=600)
    parser.add_argument("--model", default="whisper-1")
    parser.add_argument("--no-prompt", action="store_true")
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set")

    base = Path(__file__).resolve().parents[1]
    video = find_video(args.video_id)
    chunks = ensure_chunks(args.audio, args.chunk_dir, args.segment_time)
    client = OpenAI()
    prompt = None if args.no_prompt else TERMS_PROMPT

    transcript = []
    offset = 0.0
    for index, chunk in enumerate(chunks):
        chunk_duration = duration_seconds(chunk)
        cache_path = args.chunk_dir / f"{chunk.stem}.transcript.json"
        payload = transcribe_chunk(client, chunk, args.model, cache_path, prompt)
        transcript.extend(normalize_segments(payload, offset, chunk_duration))
        print(f"ok chunk {index + 1}/{len(chunks)} {chunk.name}")
        offset += chunk_duration

    transcript = drop_trailing_artifacts(transcript)
    output = write_outputs(base, video, transcript)
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
