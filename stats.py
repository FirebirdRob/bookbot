



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