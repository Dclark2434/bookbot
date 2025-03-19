def get_word_count(contents):
    word_list = contents.split()
    num_words = len(word_list)
    return num_words

def get_character_count(contents):
    chars = {}
    for char in contents:
        lowercase_char = char.lower()
        if lowercase_char in chars:
            chars[lowercase_char] += 1
        else:
            chars[lowercase_char] = 1
    return chars

def get_sorted_list(chars):
    list1 = list(chars)
    sorted_list = sorted(list1, reverse=True)
    return sorted_list
    