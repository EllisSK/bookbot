import sys
from stats import count_words, count_characters, sort_counted_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()

    return contents

def print_report(file_path):
    book_string = get_book_text(file_path)
    word_count = count_words(book_string)
    character_count = count_characters(book_string)
    sorted_dicts = sort_counted_characters(character_count)

    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {file_path}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {word_count} total words\n")
    print("--------- Character Count -------\n")
    for each_dict in sorted_dicts:
        character = each_dict["character"]
        count = each_dict["count"]
        if character.isalpha():
            print(f"{character}: {count}\n")

def main(file_path):
   print(f'{count_words(get_book_text(file_path))} words found in the document')
   print(count_characters(get_book_text(file_path)))
   print_report(file_path) 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
