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

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(chars):
    items = list(chars.items())
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    return sorted_items

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()