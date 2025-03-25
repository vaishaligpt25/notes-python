from typing import Dict


class Note:
    id: str
    subject: str
    content: str

    def __init__(self, id: str, subject: str, content: str):
        self.id = id
        self.subject = subject
        self.content = content

    @staticmethod
    def from_json_dict(json_data: Dict[str, str]) -> "Note":
        return Note(
            id=json_data["id"],
            subject=json_data["subject"],
            content=json_data["content"])
