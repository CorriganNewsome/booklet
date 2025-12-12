def __main__():
    from stats import count_words
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(word_count)

    
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents     

__main__()