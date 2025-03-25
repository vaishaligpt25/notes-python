from typing import List, Dict
from abc import ABC, abstractmethod

from src.professional_notes_app.models.note import Note


class NotesReader(ABC):

    @abstractmethod
    def read_notes(self, file_name: str) -> List[Note]:
        pass
