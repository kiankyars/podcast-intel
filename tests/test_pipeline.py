from __future__ import annotations

import json
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import Mock, patch

from podcast_intel.cli import (
    _resolve_state_path,
    _state_path,
    finalize_pipeline,
    prepare_pipeline,
)
from podcast_intel.feeds import metadata_matches, parse_feed
from podcast_intel.models import Episode, FeedConfig, Transcript
from podcast_intel.render import write_daily_digest
from podcast_intel.transcripts import (
    TranscriptUnavailable,
    _youtube_candidate_matches,
    _youtube_search_url,
    acquire_transcript,
    extract_transcript_section,
    normalize_transcript,
)


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


def semianalysis_episode() -> Episode:
    return Episode(
        id="ca0c43fba0998653a85c",
        feed_id="semianalysis-weekly",
        feed_name="SemiAnalysis Weekly",
        feed_priority=10,
        title=(
            "Ep. 028 - Most Neoclouds Suck At Security: How Agents Hacked "
            "Hugging Face (Neoclouds, Security) | Doug O'Laughlin, Sam Harshe, "
            "Jordan Nanos"
        ),
        description_html="",
        description_text="",
        published=datetime(2026, 9, 2, 14, tzinfo=timezone.utc),
        duration_seconds=3055,
        link="https://podcasters.spotify.com/pod/show/jordan-nanos/episodes/ep-028",
        audio_url="https://example.com/ep-028.mp3",
    )


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


class YouTubeMatchTests(unittest.TestCase):
    def matching_candidate(self) -> dict:
        return {
            "id": "2uU5JFJ2T-o",
            "title": (
                "Ep. 028 - Most Neoclouds Suck At Security: How Agents Hacked "
                "Hugging Face (Neoclouds, Security)"
            ),
            "channel": "SemiAnalysis",
            "duration": 3056,
        }

    def test_accepts_matching_episode_title_channel_and_duration(self) -> None:
        self.assertTrue(
            _youtube_candidate_matches(
                semianalysis_episode(),
                self.matching_candidate(),
            )
        )

    def test_rejects_different_episode_number(self) -> None:
        candidate = self.matching_candidate()
        candidate["title"] = candidate["title"].replace("028", "027", 1)
        self.assertFalse(_youtube_candidate_matches(semianalysis_episode(), candidate))

    def test_rejects_low_title_similarity(self) -> None:
        candidate = self.matching_candidate()
        candidate["title"] = "Ep. 028 - A completely unrelated weekly market recap"
        self.assertFalse(_youtube_candidate_matches(semianalysis_episode(), candidate))

    def test_rejects_wrong_channel(self) -> None:
        candidate = self.matching_candidate()
        candidate["channel"] = "Unrelated Uploads"
        self.assertFalse(_youtube_candidate_matches(semianalysis_episode(), candidate))

    def test_rejects_wrong_duration(self) -> None:
        candidate = self.matching_candidate()
        candidate["duration"] = 3792
        self.assertFalse(_youtube_candidate_matches(semianalysis_episode(), candidate))

    def test_search_accepts_matching_video(self) -> None:
        payload = {"entries": [self.matching_candidate()]}
        result = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with (
            patch("podcast_intel.transcripts.shutil.which", return_value="yt-dlp"),
            patch("podcast_intel.transcripts.subprocess.run", return_value=result),
            patch(
                "podcast_intel.transcripts._youtube_metadata",
                return_value=self.matching_candidate(),
            ),
        ):
            self.assertEqual(
                _youtube_search_url(semianalysis_episode()),
                "https://www.youtube.com/watch?v=2uU5JFJ2T-o",
            )

    def test_search_hydrates_flat_result_without_duration(self) -> None:
        flat_candidate = self.matching_candidate()
        del flat_candidate["duration"]
        payload = {"entries": [flat_candidate]}
        result = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with (
            patch("podcast_intel.transcripts.shutil.which", return_value="yt-dlp"),
            patch(
                "podcast_intel.transcripts.subprocess.run",
                return_value=result,
            ) as search,
            patch(
                "podcast_intel.transcripts._youtube_metadata",
                return_value=self.matching_candidate(),
            ) as metadata,
        ):
            self.assertEqual(
                _youtube_search_url(semianalysis_episode()),
                "https://www.youtube.com/watch?v=2uU5JFJ2T-o",
            )

        metadata.assert_called_once_with(
            "https://www.youtube.com/watch?v=2uU5JFJ2T-o"
        )
        self.assertNotIn("Doug O'Laughlin", search.call_args.args[0][-1])

    def test_search_returns_empty_when_current_video_is_not_indexed(self) -> None:
        payload = {
            "entries": [
                {
                    "id": "hj_ffVldQZA",
                    "title": (
                        "Ep. 027 - OpenAI Jalape\u00f1o: Better Than Nvidia Blackwell "
                        "(Accelerators)"
                    ),
                    "channel": "SemiAnalysis",
                    "duration": 3792,
                }
            ]
        }
        result = Mock(returncode=0, stdout=json.dumps(payload), stderr="")
        with (
            patch("podcast_intel.transcripts.shutil.which", return_value="yt-dlp"),
            patch("podcast_intel.transcripts.subprocess.run", return_value=result),
            patch(
                "podcast_intel.transcripts._youtube_metadata",
                return_value=payload["entries"][0],
            ),
        ):
            self.assertEqual(_youtube_search_url(semianalysis_episode()), "")

    def test_page_link_to_previous_episode_is_rejected_before_captions(self) -> None:
        html = (
            '<html><body><a href="https://www.youtube.com/watch?'
            'v=hj_ffVldQZA&amp;t=65s">1:05</a></body></html>'
        )
        previous_episode = {
            "id": "hj_ffVldQZA",
            "title": (
                "Ep. 027 - OpenAI Jalape\u00f1o: Better Than Nvidia Blackwell "
                "(Accelerators)"
            ),
            "channel": "SemiAnalysis",
            "duration": 3792,
        }
        with (
            patch(
                "podcast_intel.transcripts.fetch_text",
                return_value=(html, "text/html"),
            ),
            patch(
                "podcast_intel.transcripts._youtube_metadata",
                return_value=previous_episode,
            ) as metadata,
            patch("podcast_intel.transcripts._youtube_captions") as captions,
            patch("podcast_intel.transcripts._youtube_search_url", return_value=""),
        ):
            with self.assertRaisesRegex(
                TranscriptUnavailable,
                "no publisher transcript or YouTube captions found",
            ):
                acquire_transcript(semianalysis_episode(), timeout=10)

        metadata.assert_called_once_with(
            "https://www.youtube.com/watch?v=hj_ffVldQZA"
        )
        captions.assert_not_called()


class PipelineTests(unittest.TestCase):
    def test_failure_only_digest_has_typed_empty_episode_titles(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            digest_path = write_daily_digest(
                Path(temporary),
                date(2030, 6, 4),
                [],
                failed_feeds=["Fixture Show: unavailable"],
                failed_episodes=[],
            )
            digest = digest_path.read_text()
            self.assertIn("episode_titles: []", digest)
            self.assertNotIn("Processed ", digest)

    def test_state_paths_resolve_relative_and_legacy_absolute_values(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            relative = Path("episodes/2030-06-04/fixture/transcript.txt")
            absolute = root / relative

            self.assertEqual(_state_path(root, absolute), relative.as_posix())
            self.assertEqual(_state_path(root, relative), relative.as_posix())
            self.assertEqual(_resolve_state_path(root, relative), absolute)
            self.assertEqual(_resolve_state_path(root, absolute), absolute)

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
            prepared_state = json.loads((root / "data" / "state.json").read_text())
            prepared_record = next(iter(prepared_state["episodes"].values()))
            for field in (
                "analysis_path",
                "raw_transcript",
                "request_path",
                "transcript_path",
            ):
                self.assertFalse(Path(prepared_record[field]).is_absolute())
                self.assertEqual(Path(prepared_record[field]).parts[0], "episodes")
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
            digest = Path(result.digest_path).read_text()
            self.assertIn("digest: true", digest)
            self.assertIn("permalink: /", digest)
            self.assertIn('episode_titles:\n  - "OpenAI systems and new inference chips"', digest)
            self.assertIn("## TL;DR", digest)
            self.assertIn("Fixture Show · Relevance 4/5", digest)
            self.assertNotIn("# Podcast Intelligence -", digest)
            self.assertNotIn("local summary", digest)
            self.assertNotIn("Processed ", digest)
            self.assertNotIn("| relevance", digest)
            self.assertFalse((root / "digests" / "latest.md").exists())
            topic = root / "topics" / "semiconductors_compute.md"
            self.assertIn("The serving architecture changed", topic.read_text())
            state = json.loads((root / "data" / "state.json").read_text())
            record = next(iter(state["episodes"].values()))
            self.assertEqual(record["status"], "processed")
            for field in (
                "analysis_path",
                "raw_transcript",
                "request_path",
                "summary_path",
                "transcript_path",
            ):
                self.assertFalse(Path(record[field]).is_absolute())
                self.assertEqual(Path(record[field]).parts[0], "episodes")


if __name__ == "__main__":
    unittest.main()
