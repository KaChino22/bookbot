from stats import number_of_words
from stats import number_of_chars
from stats import chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = number_of_words(text)
        chars_dict = number_of_chars(text)
        sorted_chars_list = chars_dict_to_sorted_list(chars_dict) 
        print_report(book_path, num_words, sorted_chars_list)
        

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_chars_list):
    print("================ BOOKBOT ================")
    print(f"Analyzing book fount at {book_path} ...")
    print("---------------- Word Count -------------")
    print(f"Found {num_words} total words")
    print("---------------- Character Count --------")
    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("================ END =====================")


main()