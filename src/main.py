from pathlib import Path as p
from stats import get_book_text, get_num_words, get_char_counts

root_dir = p.cwd()
book_dir = p.joinpath(root_dir, "books")
book_file_path = p.joinpath(book_dir, "frankenstein.txt")


def main():
    file_contents = get_book_text(book_file_path)
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    char_counts = get_char_counts(file_contents)
    print(char_counts)


main()
