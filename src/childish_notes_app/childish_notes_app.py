import json
import os
from typing import List, Dict
from uuid import uuid4
import shortuuid


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
        # create a note object from json data
        return Note(
            id=str(json_data.get("id")),
            subject=json_data.get("subject"),
            content=json_data.get("content")
        )

    def to_json_dict(self) -> Dict[str, str]:
        # convert Note object to json dict
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
    # create an empty file in the test directory
    open(os.path.join(TEST_DIR_NAME, file_name), "w").close()
    # open(path, "w")  Opens file in write mode
    # .close()   Immediately closes the file


    # File content(notes.json):
    # [
    #     {"id": "1", "subject": "First Note", "content": "Hello"},
    #     {"id": "2", "subject": "Second Note", "content": "World"}
    # ]


def _read_all_notes(file_name: str) -> List[Note]:
    # Read all notes from the JSON file and return a list of Note objects.
    with open(os.path.join(TEST_DIR_NAME, file_name), "r") as file:
        # open file like "test_data/notes.json" in read mode
        json_data: List[Dict[str, str]] = json.load(file)
        # load json data from file
        # json_data = [
        #     { "id": "1", "subject": "First Note", "content": "Hello"},
        #     {"id": "2", "subject": "Second Note", "content": "World"}
        #    ]
        notes: List[Note] = list(map(lambda json: Note.from_json_dict(json_data=json), json_data))
        # convert json data to note objects
        # notes = [
        #     Note(id="1", subject="First Note", content="Hello"),
        #     Note(id="2", subject="Second Note", content="World")
        # ]
    return notes

def _write_all_notes(file_name: str, notes: List[Note]) -> None:
    # open file like "test_data/notes.json" in write mode
    with open(os.path.join(TEST_DIR_NAME, file_name), "w") as file:
        # Convert Note object to json dict
        json_data: List[Dict[str, str]] = list(map(lambda note: note.to_json_dict(), notes))
        # json_data = [
        #     {"id": "1", "subject": "First Note", "content": "Hello"},
        #     {"id": "2", "subject": "Second Note", "content": "World"}
        # ]
        json.dump(json_data, file, indent=2)
        # write json to file with indentation of 2 spaces

def _show_notes(notes: List[Note]) -> None:   # Takes a list of Note objects
    for note in notes:
        print(f"Id: {note.get_id()}")
        print(f"Subject: {note.get_subject()}")
        print(f"Content: {note.get_content()}")
        print()

def _show_all_notes(file_name: str) -> None:
    print("//// Showing all notes ////")
    notes: List[Note] = _read_all_notes(file_name=file_name)  # Read notes from file
    _show_notes(notes=notes)

def get_next_subject_number() -> int:
    counter_file = "subject_counter.json"      # File to store counter

    def _save_counter(number: int) -> None:
        # save the counter value to json file
        with open(counter_file, "w") as f:  # Open file for writing
            json.dump({"counter": number}, f) # Save counter as JSON

    try:
        # Read current counter from file
        with open(counter_file, "r") as f:  # Open file for reading
            data = json.load(f)   # Load JSON data
            current_number = data.get("counter", 1)  # Get counter value, default to 1

        _save_counter(current_number + 1)  # Save incremented counter
        return current_number

    # error handling:
    except FileNotFoundError:   # If file doesn't exist
        _save_counter(2)      # Create file with counter = 2
        return 1             # Return 1 as the first number

    except json.JSONDecodeError:  # If file is empty or not valid JSON
        _save_counter(2)      # Create file with counter = 2
        return 1  # Return 1 as the first number

def _input_and_create_new_note(file_name: str) -> None:
    # create a list of note object from the file
    notes: List[Note] = _read_all_notes(file_name= file_name )
    # input subject and content from user
    subject: str = input("Enter subject(or press enter for auto generate): ").strip()
    # .strip() removes whitespace from start and end
    if subject == EXIT:
        exit(0)

    if not subject:   # If subject is empty string
        subject = f"Note {get_next_subject_number()}"
    # creating new note
    new_note: Note = Note(
        id=_generate_id(),
        subject=subject,
        content=input("Enter content: ").strip()
    )
    # saving the note
    notes.append(new_note)  # Add new note to list of notes
    _write_all_notes(file_name=file_name, notes=notes)  # Save all notes to file


def _delete_note(file_name: str) -> None:
    # delete a note by ID from the specified file.
    notes: List[Note] = _read_all_notes(file_name=file_name)
    # Read existing notes from file
    if not notes:
        print("No notes to delete!")
        return
    _show_notes(notes=notes)

    # Get note ID to delete
    note_id = input("\nEnter note ID to delete : ")
    # keep all notes except the one with matching id
    notes_filtered = [note for note in notes if note.get_id() != note_id]

    if len(notes_filtered) == len(notes):
        print(f"\nNote with ID {note_id} not found!")
        return

    # save updated notes
    _write_all_notes(file_name=file_name, notes=notes_filtered)

def _edit_note(file_name: str) -> None:
    notes: List[Note] = _read_all_notes(file_name=file_name)
    _show_notes(notes=notes)

    note_id = input("Enter note ID ")
    # find the note with matching id
    note_to_edit = None
    for note in notes:
        if note.get_id() == note_id:
            note_to_edit = note
            break
    if note_to_edit is None:
        print("Note not found!")
        return
    else:
        # show current note values
        print("Note found!")
        print(f"Subject: {note_to_edit.get_subject()}")
        print(f"Content: {note_to_edit.get_content()}")
        print()

        print("Enter new values for the note:")
        new_subject = input("Enter new subject: ")
        new_content = input("Enter new content: ")
        # update notes
        note_to_edit.subject = new_subject
        note_to_edit.content = new_content
        # Save changes and show updated notes
        _write_all_notes(file_name=file_name, notes=notes)
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
            if _input_and_create_new_note(file_name=TEST_FILE_NAME ):
                print("Note created successfully")
            else:
                print("Failed to create note")
        elif choice == 3:
            if _delete_note(file_name=TEST_FILE_NAME):
                print("Note deleted successfully")
            else:
                print("Failed to delete note")
        elif choice == 4:
            if _edit_note(file_name=TEST_FILE_NAME):
                print("Note edited successfully")
            else:
                print("Failed to edit note")
        elif choice == 5:
            exit(0)
        else:
            print("Invalid choice")
