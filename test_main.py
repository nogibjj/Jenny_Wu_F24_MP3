"""Takes a csv file, reads it, and creates graphs"""

from main import main


def test_main():
    result = main()
    assert result is None


if __name__ == "__main__":
    test_main()
