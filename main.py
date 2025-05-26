from stats import get_num_words
from stats import get_num_chars
from stats import sorted_list
import sys


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    text = get_book_text(file)
    sorted = sorted_list(get_num_chars(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(file))} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()