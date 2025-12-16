import io
import re
import importlib
import sys
import unittest
from unittest.mock import patch

from test.utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_WITHOUT_COLON, REGEX_FOR_STRING


class TestExercise20(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio20"

    def run_exercise(self, input_value: str) -> list[str]:
        """Ejecuta el ejercicio con un input dado y devuelve las líneas impresas."""
        with patch("builtins.input", return_value = input_value):
            with patch("sys.stdout", new = io.StringIO()) as fake_out:
                if self.MODULE_NAME in sys.modules:
                    importlib.reload(sys.modules[self.MODULE_NAME])
                else:
                    importlib.import_module(self.MODULE_NAME)

        output = fake_out.getvalue()
        return output.strip().splitlines()

    def validateRegex(self, line: str) -> None:
        self.assertRegex(line, REGEX_FOR_LETTERS, "The print must contain a sentence explaining the result.")

    def test_string_length(self):
        lines = self.run_exercise("Hola")

        m = re.search(REGEX_FOR_INT_WITHOUT_COLON, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "4")
        self.validateRegex(lines[0])

    def test_contains_la(self):
        lines = self.run_exercise("Hola")

        m = re.search(REGEX_FOR_STRING, lines[1])
        self.assertIsNotNone(m)
        self.assertIn(m.group(1), ["True","False","Si","No","SI","NO","si","no"])
        self.validateRegex(lines[1])

    def test_uppercase(self):
        lines = self.run_exercise("Hola")

        m = re.search(REGEX_FOR_STRING, lines[2])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "HOLA")
        self.validateRegex(lines[2])

    def test_vowels_count(self):
        lines = self.run_exercise("Hola")

        m = re.search(REGEX_FOR_INT_WITHOUT_COLON, lines[3])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "2")
        self.validateRegex(lines[3])

if __name__ == '__main__':
    unittest.main()
