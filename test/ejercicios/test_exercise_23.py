import io
import re
import importlib
import sys
import unittest
from unittest.mock import patch

from test.utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING


class TestExercise23(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio23"

    def run_exercise(self, *inputs: str) -> list[str]:
        """Runs the exercise with the given inputs and captures the output."""
        with patch("builtins.input", side_effect=list(inputs)):
            with patch("sys.stdout", new = io.StringIO()) as fake_out:
                if self.MODULE_NAME in sys.modules:
                    importlib.reload(sys.modules[self.MODULE_NAME])
                else:
                    importlib.import_module(self.MODULE_NAME)

        output = fake_out.getvalue()
        return output.strip().splitlines()

    def validateRegex(self, line: str) -> None:
        self.assertRegex(line, REGEX_FOR_LETTERS, "The print must contain a sentence explaining the result.")

    def test_date_output(self):
        lines = self.run_exercise("12/06/1994")

        m = re.search(REGEX_FOR_STRING, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "94-06-12")
        self.validateRegex(lines[0])

    def test_date_output_2(self):
        lines = self.run_exercise("12/07/1994")

        m = re.search(REGEX_FOR_STRING, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "94-07-12")
        self.validateRegex(lines[0])

if __name__ == '__main__':
    unittest.main()