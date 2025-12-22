def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_num_words(file_contents):
    return len(file_contents.split())
