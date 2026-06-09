from __future__ import annotations

from pathlib import Path

from .models import Episode


def _bounded_transcript(text: str, maximum: int) -> str:
    if len(text) <= maximum:
        return text
    third = maximum // 3
    middle = len(text) // 2
    return "\n\n".join(
        (
            text[:third],
            "[TRANSCRIPT OMITTED HERE BECAUSE THE EPISODE EXCEEDED THE CONTEXT BUDGET]",
            text[middle - third // 2 : middle + third // 2],
            "[TRANSCRIPT OMITTED HERE BECAUSE THE EPISODE EXCEEDED THE CONTEXT BUDGET]",
            text[-third:],
        )
    )


def build_analysis_request(
    episode: Episode,
    transcript: str,
    profile: str,
    categories: dict[str, str],
    max_transcript_chars: int,
) -> str:
    category_text = "\n".join(
        f"- {key}: {description}" for key, description in categories.items()
    )
    bounded = _bounded_transcript(transcript, max_transcript_chars)
    return f"""Analyze this podcast episode for the private podcast intelligence system.

Write JSON only to the requested `analysis.json` file. It must match
`schemas/episode-analysis.schema.json`.

Scoring:
- 5: likely changes an important technical, company, or investment view
- 4: multiple genuinely new and consequential points
- 3: at least one useful non-obvious point
- 2: competent but mostly familiar
- 1: low signal or promotional
- 0: no useful content

For each signal:
- Attribute the claim rather than presenting it as verified fact.
- Use the closest timestamp visible in the transcript, or an empty string.
- Evidence must be a concise paraphrase, not a long quotation.
- Classify observation, inference, forecast, or opinion.
- Keep only consequential points. Seven is a hard ceiling, not a target.
- Use only these category identifiers:
{category_text}

If relevance is below 3, explain why in skip_reason. Otherwise skip_reason
should be an empty string.

READER PROFILE
--------------
{profile}

EPISODE METADATA
----------------
Episode ID: {episode.id}
Podcast: {episode.feed_name}
Title: {episode.title}
Published: {episode.published.isoformat()}
Episode URL: {episode.link}
Description: {episode.description_text[:5000]}

BEGIN TRANSCRIPT
----------------
{bounded}
--------------
END TRANSCRIPT
"""


def write_analysis_request(
    *,
    path: Path,
    episode: Episode,
    transcript: str,
    profile: str,
    categories: dict[str, str],
    max_transcript_chars: int,
) -> None:
    path.write_text(
        build_analysis_request(
            episode,
            transcript,
            profile,
            categories,
            max_transcript_chars,
        ),
        encoding="utf-8",
    )
