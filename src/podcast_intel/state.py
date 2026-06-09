from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class State:
    def __init__(self, path: Path):
        self.path = path
        self.payload: dict[str, Any] = {"version": 1, "episodes": {}}
        if path.exists():
            self.payload = json.loads(path.read_text(encoding="utf-8"))

    def get(self, episode_id: str) -> dict[str, Any]:
        return dict(self.payload["episodes"].get(episode_id, {}))

    def status(self, episode_id: str) -> str:
        return str(self.get(episode_id).get("status", ""))

    def update(self, episode_id: str, **values: Any) -> None:
        current = self.payload["episodes"].setdefault(episode_id, {})
        current.update(values)
        current["updated_at"] = datetime.now(timezone.utc).isoformat()
        self.save()

    def prune_discovered(self) -> None:
        episode_ids = [
            episode_id
            for episode_id, record in self.payload["episodes"].items()
            if record.get("status") == "discovered"
        ]
        if not episode_ids:
            return
        for episode_id in episode_ids:
            del self.payload["episodes"][episode_id]
        self.save()

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(
            json.dumps(self.payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, self.path)
