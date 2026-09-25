import unittest

from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def test_run_main_noargs(self) -> None:
        result = run_python_file("calculator", "main.py")
        print(f"{result}\n")

    def test_run_main_args(self) -> None:
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(f"{result}\n")

    def test_run_tests(self) -> None:
        result = run_python_file("calculator", "tests.py")
        print(f"{result}\n")

    def test_run_outside_main(self) -> None:
        result = run_python_file("calculator", "../main.py")
        print(f"{result}\n")

    def test_run_nonexistent(self) -> None:
        result = run_python_file("calculator", "nonexistent.py")
        print(f"{result}\n")

    def test_run_normal_file(self) -> None:
        result = run_python_file("calculator", "lorem.txt")
        print(f"{result}\n")

if __name__ == "__main__":
    unittest.main()