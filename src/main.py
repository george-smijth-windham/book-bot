from pathlib import Path as p
from stats import (
    get_book_text,
    get_num_words,
    get_char_counts,
    get_sorted_char_counts,
    get_report,
)

ROOT_DIR = p.cwd()
BOOK_DIR = p.joinpath(ROOT_DIR, "books")
BOOK_FILE_PATH = p.joinpath(BOOK_DIR, "frankenstein.txt")


def main():
    file_contents = get_book_text(BOOK_FILE_PATH)
    num_words = get_num_words(file_contents)
    char_counts = get_char_counts(file_contents)
    report = get_report(num_words, char_counts)
    print(report)


main()
