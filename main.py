from stats import get_num_words, sort_on, get_chars_dict



def main():

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    sorted_items = sort_on(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")

    for char, freq in sorted_items:
        print(f"The '{char}' character was found {freq} times")



def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()