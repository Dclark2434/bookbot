def get_book_text(book_path):
    with open(book_path) as f:
        contents = f.read()
    return contents

def main():
    return print(get_book_text("./books/frankenstein.txt"))

main()