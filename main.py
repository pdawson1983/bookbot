def main():
    frankenstein_string = get_book_string("books/frankenstein.txt")
    print(f"{count_words(frankenstein_string)} words in the book.")
    print(count_char(frankenstein_string))

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