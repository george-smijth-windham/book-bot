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


def sort_on(char):
    return char["num"]


def get_sorted_char_counts(char_counts):
    chars = []
    for c, count in char_counts.items():
        if c.isalpha():
            chars.append({"char": c, "num": count})
    chars.sort(reverse=True, key=sort_on)
    return chars


def get_char_count_string(sorted_char_counts):
    char_count_str = ""
    for i in range(len(sorted_char_counts)):
        c, count = sorted_char_counts[i].values()
        char_count_str = (
            f"{c}: {count}" if not char_count_str else f"{char_count_str}\n{c}: {count}"
        )
    return char_count_str


def get_report(*args):
    num_words, char_counts = args
    output = ""
    sorted_char_counts = get_sorted_char_counts(char_counts)
    char_count_string = get_char_count_string(sorted_char_counts)
    output = output + "============ BOOKBOT ============"
    output = output + f"\nAnalyzing book found at books/frankenstein.txt..."
    output = output + f"\n----------- Word Count ----------"
    output = output + f"\nFound {num_words} total words"
    output = output + f"\n--------- Character Count -------"
    output = output + f"\n{char_count_string}"
    output = output + f"\n============= END ==============="
    return output
