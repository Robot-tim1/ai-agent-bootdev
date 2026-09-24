import unittest

from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_lorem(self) -> None:
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")

    def test_main(self) -> None:
        result = get_file_content("calculator", "main.py")
        print(f"{result}\n")

    def test_pkg_calculator(self) -> None:
        result = get_file_content("calculator", "pkg/calculator.py")
        print(f"{result}\n")

    def test_outside_file(self) -> None:
        result = get_file_content("calculator", "/bin/cat")
        print(f"{result}\n")

    def test_not_exist(self) -> None:
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(f"{result}\n")

if __name__ == "__main__":
    unittest.main()