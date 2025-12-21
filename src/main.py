from pathlib import Path as p

root_dir = p.cwd()
book_dir = p.joinpath(root_dir, "books")
book_file_path = p.joinpath(book_dir, "frankenstein.txt")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_num_words(file_contents):
    return len(file_contents.split())


def main():
    file_contents = get_book_text(book_file_path)
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")


main()
