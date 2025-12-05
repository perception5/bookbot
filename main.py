
import sys
from stats import word_count
from stats import letter_tally
from stats import sort_tally

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    get_text = get_book_text(book_path)
    words_counted = word_count(get_text)
    letters_counted = letter_tally(get_text)
    sorted_tally = sort_tally(letters_counted)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_counted} total words")
    print("----------- Character Count ----------")
    for entry in sorted_tally:
        char = entry["char"]
        if char.isalpha():
            print(f"{char}: {entry['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()    

main()
