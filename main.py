def main(book):
    book = get_book_string("books/frankenstein.txt")
    display_header(book)
    print(f"{count_words(book)} words in the book.")
    print(count_char(book))


def display_header(book_path):
    print(f"+++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Analysis for text at {book_path}")
    print(f"+++++++++++++++++++++++++++++++++++++++++++++")


def get_book_string(book_location):
    with open(book_location) as f:
        book_string = f.read()
        return book_string

def count_words(book_string):
    return len(book_string.split())

def count_char(book_string):
    character_dict = {}
    for character in book_string.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

main()