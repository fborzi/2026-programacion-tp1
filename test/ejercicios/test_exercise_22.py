import io
import re
import importlib
import sys
import unittest
from unittest.mock import patch

from test.utils.constant import REGEX_FOR_FLOAT_INT, REGEX_FOR_LETTERS, REGEX_FOR_STRING


class TestExercise22(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio22"

    def run_exercise(self, *inputs: int) -> list[str]:
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

    def test_sum(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "160")
        self.validateRegex(lines[0])

    def test_division(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[1])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "15.0")
        self.validateRegex(lines[1])

    def test_division_fail(self):
        lines = self.run_exercise(150, 0)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[2])
        self.assertIsNotNone(m)
        self.assertEqual(len(lines), 5, "Its not informed to the user that division by zero is not possible.")
        self.assertEqual(m.group(1), "0.0")
        self.validateRegex(lines[2])

    def test_is_divisible(self):
        lines = self.run_exercise(150, 12)

        m = re.search(REGEX_FOR_STRING, lines[2])
        self.assertIsNotNone(m)
        self.assertIn(m.group(1), ["True", "False"])
        self.validateRegex(lines[2])

    def test_is_divisible_fail(self):
        lines = self.run_exercise(150, 0)

        m = re.search(REGEX_FOR_STRING, lines[3])
        self.assertIsNotNone(m)
        self.assertEqual(len(lines), 5, "Its not informed to the user that division by zero is not possible.")
        self.assertEqual(m.group(1), "False")
        self.validateRegex(lines[3])

    def test_percentage(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[3])
        print(m)
        self.assertIsNotNone(m)

        self.assertEqual(m.group(1), "15")
        self.validateRegex(lines[3])

    def test_percentage_fail(self):
        lines = self.run_exercise(150, 0)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[4])
        print(m)
        self.assertIsNotNone(m)
        self.assertEqual(len(lines), 5, "Its not informed to the user that division by zero is not possible.")
        self.assertEqual(m.group(1), "0")
        self.validateRegex(lines[4])

if __name__ == '__main__':
    unittest.main()