import json
import os
from typing import List, Dict
from uuid import uuid4
import shortuuid

# Generate a short UUID
short_id = shortuuid.ShortUUID().random(length=8)
print(short_id)



"""
JSON file format

[
    {
        "id": "1",
        "subject": "My first note title",
        "content": "Today is 15th March, yesterday we played Holi"
    },
    {
        "id": "2",
        "subject": "Daily log - 2",
        "content": "Yesterday we had visited and made plans to goto FlipSide, today we are too tired and gave up."
    }
]

"""
# Class Definition:
class Note:
    id: str
    subject: str
    content: str

# Constructor Method:
    def __init__(self,
                 id: str,
                 subject: str,
                 content: str) -> None:
        self.id: str = id
        self.subject: str = subject
        self.content: str = content

    # Static Method:
    @staticmethod
    def from_json_dict(json_data: Dict[str, str]) -> 'Note':
        return Note(
            id=str(json_data.get("id")),
            subject=json_data.get("subject"),
            content=json_data.get("content")
        )

    def to_json_dict(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "subject": self.subject,
            "content": self.content
        }

    def get_id(self) -> str:
        return self.id

    def get_subject(self) -> str:
        return self.subject

    def get_content(self) -> str:
        return self.content

TEST_DIR_NAME: str = "data"
TEST_FILE_NAME: str = "notes_1.json"
EXIT: str = "exit"

short_id = shortuuid.ShortUUID().random(length=8)

def _generate_id() -> str:
    short_id = shortuuid.ShortUUID().random(length=8)
    return str(short_id)

def _create_empty_json_file(file_name: str) -> None:
    open(os.path.join(TEST_DIR_NAME, file_name), "w").close()

def _read_all_notes(file_name: str) -> List[Note]:
    with open(os.path.join(TEST_DIR_NAME, file_name), "r") as file:
        json_data: List[Dict[str, str]] = json.load(file)
        notes: List[Note] = list(map(lambda json: Note.from_json_dict(json_data=json), json_data))
    return notes

def _write_all_notes(file_name: str, notes: List[Note]) -> None:
    with open(os.path.join(TEST_DIR_NAME, file_name), "w") as file:
        json_data: List[Dict[str, str]] = list(map(lambda note: note.to_json_dict(), notes))
        json.dump(json_data, file, indent=2)

def _show_notes(notes: List[Note]) -> None:
    for note in notes:
        print(f"Id: {note.get_id()}")
        print(f"Subject: {note.get_subject()}")
        print(f"Content: {note.get_content()}")
        print()

def _show_all_notes(file_name: str) -> None:
    print("//// Showing all notes ////")
    notes: List[Note] = _read_all_notes(file_name=file_name)
    _show_notes(notes=notes)

def _input_and_create_new_note(file_name: str) -> None:
    notes: List[Note] = _read_all_notes(file_name=TEST_FILE_NAME)

    # input subject and content from user
    subject: str = input("Enter subject: ")
    if subject == EXIT:
        exit(0)
    new_note: Note = Note(
        id=_generate_id(),
        subject=subject,
        content=input("Enter content: "))

    notes.append(new_note)
    _write_all_notes(file_name=TEST_FILE_NAME, notes=notes)


def _delete_note(file_name: str) -> None:
    notes: List[Note] = _read_all_notes(file_name=file_name)

    if not notes:
        print("No notes to delete!")
        return

    print("\nAvailable notes:")
    _show_notes(notes=notes)

    note_id = input("\nEnter note ID to delete (or 'cancel' to go back): ")
    if note_id.lower() == 'cancel':
        return

    # Find and delete the note
    notes_filtered = [note for note in notes if note.get_id() != note_id]

    if len(notes_filtered) == len(notes):
        print(f"\nNote with ID {note_id} not found!")
        return

    _write_all_notes(file_name=file_name, notes=notes_filtered)
    # print("\nNote deleted successfully!")

def _edit_note(file_name: str) -> None:
    notes: List[Note] = _read_all_notes(file_name=file_name)

    _show_notes(notes=notes)
    note_id = input("Enter note ID ")
    note_to_edit = None
    for note in notes:
        if note.get_id() == note_id:
            note_to_edit = note
            break
    if note_to_edit is None:
        print("Note not found!")
        return
    else:
        print("Note found!")
        print(f"Subject: {note_to_edit.get_subject()}")
        print(f"Content: {note_to_edit.get_content()}")
        print()

        print("Enter new values for the note:")
        new_subject = input("Enter new subject: ")
        new_content = input("Enter new content: ")
        note_to_edit.subject = new_subject
        note_to_edit.content = new_content
        _write_all_notes(file_name=file_name, notes=notes)
        # print("\nNote edited successfully!")
        _show_notes(notes=notes)


if __name__ == '__main__':
    while True:
        print("-------Notes-app-------")
        print("1. Show all notes")
        print("2. Create new note")
        print("3. Delete note")
        print("4. Edit Note")
        print("5. Exit")

        choice: int = int(input("Enter your choice: "))
        print("------------------")
        if choice == 1:
            _show_all_notes(file_name=TEST_FILE_NAME)
        elif choice == 2:
            _input_and_create_new_note(file_name=TEST_FILE_NAME)
            print("Note created successfully")
        elif choice == 3:
            _delete_note(file_name=TEST_FILE_NAME)
            print("Note deleted successfully")
        elif choice == 4:
            _edit_note(file_name=TEST_FILE_NAME)
            print("Note edited successfully")
        elif choice == 5:
            exit(0)
        else:
            print("Invalid choice")
