from typing import List, override
from src.professional_notes_app.notes_writer import NotesWriter
import json

class JsonNotesWriter(NotesWriter):
    @override
    def write_notes(self, file_name: str, notes: List[str]) -> None:
        data = {'notes': notes}
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)