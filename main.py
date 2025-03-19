from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_char_counts
import sys

# Checks if there is a book parameter included in execution line and educates user.
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

def main():
    book_path = sys.argv[1]
    contents = get_book_text(book_path)
    num_words = get_word_count(contents)
    char_count = get_character_count(contents)
    sorted_char_counts = get_sorted_char_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("------ Character Count ----------")
    for letter in sorted_char_counts:
        print(f"{letter['char']}: {letter['count']}")
    print("============== END ==============")

main()