import io
import re
import importlib
import sys
import unittest

from unittest.mock import patch
from test.utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_ONLY, REGEX_FOR_STRING, REGEX_FOR_INT_WITHOUT_COLON


class TestExercise21(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio21"

    def run_exercise(self, *inputs: str) -> list[str]:
        """Ejecuta el ejercicio con un input dado y devuelve las líneas impresas."""
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

    def test_count_strings(self):
        lines = self.run_exercise("Hola", "Hola Mundo hacia la Hola")

        m = re.search(REGEX_FOR_INT_ONLY, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "2")
        self.validateRegex(lines[0])

    def test_strings_concatenated(self):
        lines = self.run_exercise("Hola", "Hola Mundo hacia la Hola")

        m = re.search(REGEX_FOR_STRING, lines[1])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "holahola mundo hacia la hola")
        self.validateRegex(lines[1])

    def test_letter_from_string1_in_string2(self):
        lines = self.run_exercise("Hola", "Hola Mundo hacia la Hola")

        m = re.search(REGEX_FOR_INT_WITHOUT_COLON, lines[2])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "3")
        self.validateRegex(lines[2])


if __name__ == '__main__':
    unittest.main()
