import sys
from stats import ( 
    get_book_text,
    get_number_words,
    get_character_count,
    char_dict_to_sorted_list
    )


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_number_words(text)
    char_counts = get_character_count(text)
    sorted_chars = char_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():  
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

main()
