def get_word_count(contents):
    word_list = contents.split()
    num_words = len(word_list)
    return num_words

def get_character_count(contents):
    char_counts_dict = {}
    for char in contents:
        lowercase_char = char.lower()
        if lowercase_char in char_counts_dict:
            char_counts_dict[lowercase_char] += 1
        else:
            char_counts_dict[lowercase_char] = 1
    return char_counts_dict

def get_sorted_char_counts(char_counts_dict):
    char_list = []
    for char, count in char_counts_dict.items():
        if char.isalpha() == True:
            char_list.append({'char': char, 'count': count})
            
    char_list.sort(key=lambda item: item['count'], reverse=True)
    return char_list
