from stats import get_num_words, sort_on, get_chars_dict
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    sorted_items = sort_on(chars_dict)
    print(f"--- Begin report of {book_path} ---")

    for char, freq in sorted_items:
        print(f"{char}: {freq}")



def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()