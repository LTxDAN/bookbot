# functions for analyzing the text

def get_book_text(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as file:
        return file.read()

def get_number_words(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> dict[str, int]:
    text = text.lower()
    letters_count: dict[str, int] = {}
    for ch in text:
        if ch in letters_count:
            letters_count[ch] += 1
        else:
            letters_count[ch] = 1
    return letters_count

def sort_on_number(item: dict) -> int:
    return item["num"]

def char_dict_to_sorted_list(char_counts: dict[str, int]) -> list[dict]:
    items = [{"char": ch, "num": n} for ch, n in char_counts.items()]
    items.sort(key=sort_on_number, reverse=True)
    return items
