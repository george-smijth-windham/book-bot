from pathlib import Path as p
from stats import (
    get_book_text,
    get_num_words,
    get_char_counts,
    get_report,
)
import sys


ROOT_DIR = p.cwd()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    _, book_name = sys.argv
    book_file_path = p.joinpath(ROOT_DIR, book_name)
    book_contents = get_book_text(book_file_path)
    book_num_words = get_num_words(book_contents)
    book_char_counts = get_char_counts(book_contents)
    book_report = get_report(book_num_words, book_char_counts, book_name)
    print(book_report)


main()
