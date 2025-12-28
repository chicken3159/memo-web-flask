import json
from pathlib import Path
from typing import List, Dict, Any

class JsonMemoStorage:
    def __init__(self, filename: str):
        base_dir = Path(__file__).resolve().parent
        self.filepath = base_dir / filename

    def load(self) -> List[Dict[str, Any]]:
        if not self.filepath.exists():
            return []
        try:
            with self.filepath.open("r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []

    def save(self, memos: List[Dict[str, Any]]) -> None:
        with self.filepath.open("w", encoding="utf-8") as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)

