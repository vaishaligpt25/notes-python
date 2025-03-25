from typing import List
from abc import ABC, abstractmethod

class NotesWriter(ABC):
    @abstractmethod
    def write_notes(self, file_name: str, notes: List[str]) -> None:
        pass
