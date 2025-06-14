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
