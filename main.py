def main(book_location="books/frankenstein.txt"):
    book = get_book_string(book_location)
    display_header(book_location)
    print(f"{count_words(book)} words in the book.")
    display_char(count_char_dict(book))


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

def count_char_dict(book_string):
    character_dict = {}
    for character in book_string:
        if character.isalpha():
            character_lower = character.lower()
            if character_lower in character_dict:
                character_dict[character_lower] += 1
            else:
                character_dict[character_lower] = 1
    sorted_character_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True ))
    return sorted_character_dict

def display_char(char_dict):
    for character in char_dict:
        print(f"The'{character}' character was found {char_dict[character]} times")

main()