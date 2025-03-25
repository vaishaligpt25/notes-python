import unittest
from typing import List
from parameterized import parameterized
from src.professional_notes_app.notes_reader.json_notes_reader import JsonNotesReader


class TestJsonNotesReader(unittest.TestCase):

    def setUp(self) -> None:
        self.subject: JsonNotesReader = JsonNotesReader()


    @parameterized.expand([
        ("empty_file", "test1.json", []),
        ("single_note", "test2.json", [{"id": "1", "subject": "test", "content": "Content"}]),
        ("multiple_notes", "test3.json", [
            {"id": "1", "subject": "Test1", "content": "Content1"},
            {"id": "2", "subject": "Test2", "content": "Content2"}])
        ])

    def test_read_notes(self,
                        scenario_name: str,
                        file_name: str,
                        expected_result: List[dict]) -> None:

        result = self.subject.read_notes(file_name=file_name)
        self.assertEqual(expected_result, result)






