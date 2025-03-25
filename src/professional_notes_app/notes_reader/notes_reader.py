from typing import List, Dict
from abc import ABC, abstractmethod

class Note(ABC):
    id: str
    subject: str
    content: str

    def __init__(self, id: str, subject: str, content: str):
        self.id = id
        self.subject = subject
        self.content = content

    @staticmethod
    def from_json_dict(json_data: Dict[str, str]):
        return Note(
            id=json_data["id"],
            subject=json_data["subject"],
            content=json_data["content"])
class NotesReader(ABC):

    @abstractmethod
    def read_notes(self, file_name: str) -> List[Note]:
        pass
