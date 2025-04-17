def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_chars(text):
    chars = {}
    for c in text: 
        lowered_c = c.lower()
        if lowered_c in chars:
            chars[lowered_c] += 1
        else:
            chars[lowered_c] = 1
    return chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
