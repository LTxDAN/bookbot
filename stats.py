# functions for analyzing the text
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents
    
def get_number_words():
    words = get_book_text("books/frankenstein.txt")
    num_words = len(words.split())
    return num_words

def get_character_count():
    book_string = get_book_text("books/frankenstein.txt")
    book_string = book_string.lower()
    letters_count = {}
    for ch in book_string:
        if ch in letters_count:
            letters_count[ch] += 1
        else:
            letters_count[ch] = 1
    return letters_count
