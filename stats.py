def count_words(words_string):
    n_words = len(words_string.split())
    return n_words

def count_characters(words_string):
    char_dict = {}
    words_string = words_string.lower()
    for character in words_string:
        try:
            char_dict[character] += 1
        except:
            char_dict[character] = 1

    return char_dict

def sort_on(dict):
    return dict["count"]

def sort_counted_characters(char_dict):
    char_dict_list = []
    for item in char_dict:
        char_dict_list.append({"character" : item, "count" : char_dict[item]})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list
