# Dylan Patel 2026 Podcast Transcripts

This directory contains original 2026 Dylan Patel podcast/interview/conversation transcripts fetched from YouTube captions with `uv tool run youtube_transcript_api`, plus supplemental 2025 a16z and Yesterday Podcast episodes requested by the user.

Use `index.json` as the machine-readable manifest. Each transcript is saved twice:

- `transcripts/*.json`: metadata plus timestamped caption segments.
- `transcripts/*.md`: readable timestamped transcript text.

Clips, reuploads, summaries, and short TV/event excerpts are listed in `index.json` under `skipped_candidates` instead of mixed into the corpus.
