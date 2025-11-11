from stats import count_words, count_characters, print_header, print_foot, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    String = get_book_text(sys.argv[1])
    num_words = count_words(String)
    print_header("books/frankenstein.txt", num_words)
    for item in sort_dict(count_characters(String)):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print_foot()        

main()    