from typing import List, Dict, override
from src.professional_notes_app.notes_reader.notes_reader import NotesReader, Note
import json
import os

class JsonNotesReader(NotesReader):
    @override()
    def read_notes(self, file_name: str) -> List[Note]:
        # Read all notes from the JSON file and return a list of Note objects.
        if not file_name:
            raise ValueError("File name cannot be empty")
        if not os.path.exists(file_name):
            raise FileNotFoundError(f"File not found: {file_name}")

        with open(file_name, "r") as file:
            json_data: List[Dict[str, str]] = json.load(file)
            notes: List[Note] = list(map(lambda json: Note.from_json_dict(json_data=json), json_data))
            return notes





