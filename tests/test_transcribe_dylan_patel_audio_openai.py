import tempfile
import unittest
from pathlib import Path

from scripts.transcribe_dylan_patel_audio_openai import (
    TERMS_PROMPT,
    resolve_chunk_dir,
)


class ChunkDirectoryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name) / "repo"
        self.audio = Path(self.temporary.name) / "episode.mp3"
        self.audio.write_bytes(b"original audio")

    def resolve(self, **overrides):
        values = {
            "chunk_dir": None,
            "base": self.base,
            "audio_path": self.audio,
            "video_id": "video-id",
            "segment_time": 600,
            "model": "whisper-1",
            "prompt": TERMS_PROMPT,
        }
        values.update(overrides)
        return resolve_chunk_dir(**values)

    def test_default_is_stable_and_repo_local(self):
        first = self.resolve()
        second = self.resolve()

        self.assertEqual(first, second)
        self.assertEqual(
            first.parent,
            self.base / "data" / "cache" / "dylan-audio" / "video-id",
        )
        self.assertRegex(first.name, r"^[0-9a-f]{64}$")

    def test_fingerprint_changes_with_audio_and_transcription_settings(self):
        baseline = self.resolve()

        self.audio.write_bytes(b"changed audio")
        changed_audio = self.resolve()
        self.audio.write_bytes(b"original audio")

        variants = {
            changed_audio,
            self.resolve(segment_time=300),
            self.resolve(model="gpt-4o-transcribe"),
            self.resolve(prompt=None),
            self.resolve(prompt=TERMS_PROMPT + " Extra vocabulary."),
        }

        self.assertEqual(len(variants), 5)
        self.assertNotIn(baseline, variants)

    def test_explicit_chunk_directory_is_preserved_without_reading_audio(self):
        explicit = Path(self.temporary.name) / "chosen-chunks"
        missing_audio = Path(self.temporary.name) / "missing.mp3"

        resolved = self.resolve(chunk_dir=explicit, audio_path=missing_audio)

        self.assertEqual(resolved, explicit)


if __name__ == "__main__":
    unittest.main()
