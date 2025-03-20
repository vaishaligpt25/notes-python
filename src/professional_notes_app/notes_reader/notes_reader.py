from typing import List
from abc import ABC, abstractmethod


class NotesReader(ABC):
    @abstractmethod
    def read_notes(self, file_name: str) -> List[str]:
        pass
