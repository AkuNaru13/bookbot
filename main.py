import sys
from stats import get_num_words,get_char_count,sort_char_counts

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
       return file.read()


def count_words(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)

    char_count = get_char_count(book_text)
    sorted_chars = sort_char_counts(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()