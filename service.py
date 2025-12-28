from typing import List, Dict, Any

class MemoService:
    def __init__(self, storage):
        self.storage = storage

    def list_memos(self) -> List[Dict[str, Any]]:
        return self.storage.load()

    def add_memo(self, text: str) -> Dict[str, Any]:
        memos = self.storage.load()
        next_id = (max([m.get("id", 0) for m in memos]) + 1) if memos else 1
        memo = {"id": next_id, "text": text}
        memos.append(memo)
        self.storage.save(memos)
        return memo

    def delete_memo(self, memo_id: int) -> bool:
        memos = self.storage.load()
        new_memos = [m for m in memos if m.get("id") != memo_id]
        if len(new_memos) != len(memos):
            self.storage.save(new_memos)
            return True
        return False

    def update_memo(self, memo_id: int, new_text: str) -> bool:
        memos = self.storage.load()
        for m in memos:
            if m.get("id") == memo_id:
                m["text"] = new_text
                self.storage.save(memos)
                return True
        return False

