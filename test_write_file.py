import unittest

from functions.write_file import write_file

class TestGetFileInfo(unittest.TestCase):
    # Uncomment this when you need to submit
    #def test_write_lorem(self) -> None:
    #    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #    print(f"{result}\n")

    def test_write_new_file(self) -> None:
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(f"{result}\n")

    def test_write_outside(self) -> None:
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(f"{result}\n")

if __name__ == "__main__":
    unittest.main()