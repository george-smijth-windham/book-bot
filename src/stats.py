def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_num_words(file_contents):
    return len(file_contents.split())


def get_char_counts(file_contents):
    char_counts = {}

    for char in file_contents:
        c = char.lower()
        if c not in char_counts:
            char_counts[c] = 0
        char_counts[c] += 1
    return char_counts
