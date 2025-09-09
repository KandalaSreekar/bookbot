from stats import no_of_words, dict_word_count, report_of_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text_path = sys.argv[1]
        # frankenstein_contents = get_book_text("books/frankenstein.txt")
        frankenstein_contents = get_book_text(text_path)
        word_count = no_of_words(frankenstein_contents)
        # print(f"{word_count} words found in the document")
        letter_count = dict_word_count(frankenstein_contents)
        # print(letter_count)
        sorted_dicts = report_of_dict(letter_count)
        # print(sorted_dicts)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("----------- Character Count ----------")
        for dict in sorted_dicts:
            if dict["char"].isalpha():
                print(f"{dict['char']}: {dict['num']}")



main()