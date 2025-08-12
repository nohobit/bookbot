import sys

#Import Stats Functions
from stats import get_letter_count
from stats import sort_letter_count
from stats import get_num_words

#Print Report
def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]
        char_count = get_letter_count(file)
        number_of_words = get_num_words(file)
        sorted_counts = sort_letter_count(char_count)
        formatted_counts = ""
        for k, v in sorted_counts.items():
            if k.isalpha():
                formatted_counts += f"{k}: {v}\n"
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("---------- Character Count ---------")
        print(formatted_counts)
        print("============== END ==============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()