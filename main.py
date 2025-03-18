from stats import get_word_count
from stats import get_character_count

def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

def main():
    contents = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(contents)
    char_count = get_character_count(contents)
    print(f"{num_words} words found in the document")

main()