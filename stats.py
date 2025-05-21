def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_char_counts(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list