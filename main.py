from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()

    return contents

def main():
   print(f'{count_words(get_book_text("books/frankenstein.txt"))} words found in the document')
   print(count_characters(get_book_text("books/frankenstein.txt")))

main()
