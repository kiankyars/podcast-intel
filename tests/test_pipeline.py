from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from podcast_intel.cli import finalize_pipeline, prepare_pipeline
from podcast_intel.feeds import metadata_matches, parse_feed
from podcast_intel.models import FeedConfig, Transcript
from podcast_intel.transcripts import extract_transcript_section, normalize_transcript


RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
  xmlns:podcast="https://podcastindex.org/namespace/1.0">
  <channel>
    <title>Fixture Show</title>
    <item>
      <title>OpenAI systems and new inference chips</title>
      <description><![CDATA[
        A first-party discussion about model serving and semiconductor design.
      ]]></description>
      <link>https://example.com/episode</link>
      <guid>fixture-1</guid>
      <pubDate>Thu, 04 Jun 2030 16:14:49 GMT</pubDate>
      <enclosure url="https://example.com/audio.mp3" type="audio/mpeg"/>
      <itunes:duration>01:10:00</itunes:duration>
      <podcast:transcript
        url="https://example.com/transcript.vtt"
        type="text/vtt"
        rel="captions"/>
    </item>
  </channel>
</rss>
"""


class FeedTests(unittest.TestCase):
    def test_parse_feed_and_metadata_filter(self) -> None:
        feed = FeedConfig(
            id="fixture",
            name="Fixture Show",
            url="file:///fixture.rss",
            mode="filtered",
            priority=7,
        )
        episodes = parse_feed(RSS, feed)
        self.assertEqual(len(episodes), 1)
        episode = episodes[0]
        self.assertEqual(episode.duration_seconds, 4200)
        self.assertEqual(episode.transcript_urls[0]["type"], "text/vtt")
        self.assertTrue(metadata_matches(episode, feed, ("openai",)))

    def test_caption_normalization(self) -> None:
        vtt = """WEBVTT

00:00:01.000 --> 00:00:03.000
The first point.

00:00:05.000 --> 00:00:07.000
The second point.
"""
        self.assertEqual(
            normalize_transcript(vtt, "text/vtt"),
            "[00:00:01] The first point.\n[00:00:05] The second point.",
        )

    def test_extract_embedded_transcript(self) -> None:
        source = "Show notes\n\nTranscript\n\nSpeaker: " + ("useful detail " * 200)
        extracted = extract_transcript_section(source)
        self.assertTrue(extracted.startswith("Speaker:"))
        self.assertNotIn("Show notes", extracted)

    def test_chapter_list_is_not_a_transcript_heading(self) -> None:
        from podcast_intel.transcripts import has_transcript_heading

        source = "Episode notes\n\n(00:00) Intro\n\n(05:00) Technical discussion"
        self.assertFalse(has_transcript_heading(source))


class PipelineTests(unittest.TestCase):
    def test_offline_pipeline_writes_digest_topics_and_state(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            feed_path = root / "fixture.rss"
            feed_path.write_text(RSS, encoding="utf-8")
            (root / "profile.md").write_text("Prefer technical specifics.\n")
            (root / "config.toml").write_text(
                f"""
[run]
lookback_days = 30
max_episodes = 3
max_total_hours = 8.0
min_relevance_score = 3
request_timeout_seconds = 10
max_transcript_chars = 100000

[selection]
keywords = ["openai"]

[categories]
semiconductors_compute = "Compute."

[[feeds]]
id = "fixture"
name = "Fixture Show"
url = "{feed_path.as_uri()}"
mode = "filtered"
priority = 7
""".strip()
                + "\n",
                encoding="utf-8",
            )

            def fake_transcript(*args, **kwargs):
                return Transcript(
                    text="[00:01] A genuinely new inference architecture detail. " * 80,
                    source="fixture",
                    source_url="https://example.com/transcript",
                )

            prepared = prepare_pipeline(
                root=root,
                transcript_acquirer=fake_transcript,
            )
            self.assertEqual(prepared.selected, 1)
            pending = json.loads((root / "data" / "pending_analysis.json").read_text())
            analysis = {
                "relevance_score": 4,
                "summary": "The guest described a concrete inference design change.",
                "why_it_matters": "It changes expected serving cost.",
                "signals": [
                    {
                        "category": "semiconductors_compute",
                        "claim": "The serving architecture changed.",
                        "evidence": "The guest tied the change to lower memory traffic.",
                        "timestamp": "00:01",
                        "confidence": "high",
                        "kind": "observation",
                    }
                ],
                "entities": ["OpenAI"],
                "changed_views": [],
                "follow_ups": ["Check measured serving cost."],
                "skip_reason": "",
            }
            Path(pending[0]["analysis_path"]).write_text(json.dumps(analysis), encoding="utf-8")

            result = finalize_pipeline(root=root)
            self.assertEqual(result.relevant, 1)
            self.assertTrue(Path(result.digest_path).exists())
            topic = root / "topics" / "semiconductors_compute.md"
            self.assertIn("The serving architecture changed", topic.read_text())
            state = json.loads((root / "data" / "state.json").read_text())
            record = next(iter(state["episodes"].values()))
            self.assertEqual(record["status"], "processed")


if __name__ == "__main__":
    unittest.main()
