import unittest

from functions.get_files_info import get_files_info

class TestGetFileInfo(unittest.TestCase):
    def test_current(self) -> None:
        result = get_files_info("calculator", ".")
        print(f"{result}\n")

    def test_outside_workingdir(self) -> None:
        result = get_files_info("calculator", "/bin")
        print(f"{result}\n")

    def test_relative_outside_workingdir(self) -> None:
        result = get_files_info("calculator", "../")
        print(f"{result}\n")

    def test_file_in_dir(self) -> None:
        result = get_files_info("calculator", "pkg")
        print(f"{result}\n")

if __name__ == "__main__":
    unittest.main()