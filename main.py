import sys
from stats import count_words, num_chars, report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    number_of_chars = num_chars(book_text)
    sorted_list = report(number_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents     

def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

main()