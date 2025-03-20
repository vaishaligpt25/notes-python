from typing import List, Dict, override
from src.professional_notes_app.notes_reader.notes_reader import NotesReader
import json
import os

class JsonNotesReader(NotesReader):
    @override
    def read_notes(self, file_name: str) -> List[str]:
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File {file_name} not found")
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data.get("notes", [])

