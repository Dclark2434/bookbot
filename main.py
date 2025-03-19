from stats import get_word_count
from stats import get_character_count
from stats import get_sorted_char_counts

def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

def main():
    book_path = "books/frankenstein.txt"
    contents = get_book_text(f"./{book_path}")
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