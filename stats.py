
def convert_book_to_string(filepath):
    with open(filepath) as ftoread:
        read = ftoread.read()
        content = str(read)
    return content

def get_num_words(filepath):
    bstring = convert_book_to_string(filepath)
    word_count = len(bstring.split())
    return word_count

def get_letter_count(filepath) -> dict[str, int]:
    bstring = convert_book_to_string(filepath)
    tolower = bstring.lower()
    counts = {}
    for char in tolower:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_letter_count(letter_count: dict[str, int]) -> dict[str, int]:
    sorted_counts = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts