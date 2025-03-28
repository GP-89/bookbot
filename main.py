import sys
from stats import get_num_words
from stats import count_characters
from stats import report

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit the program if no file path is provided


def get_book_text(path):
    """
    This function reads the content of a book file and returns it as a string.
    """
    with open(sys.argv[1]) as f: # Open the book file in read mode
        content = f.read() # Read the entire content of the file
    return content # Return the content as a string

def main():
    book_path = 'books/frankenstein.txt'  # Path to the book file
    book_text = get_book_text(book_path) # Call the function to read the book content

    print(f"============ BOOKBOT ============\n")  # Print the title of the program
    print(f"Analyzing book found at {book_path}...\n")  # Print the title of the program
    print(f"----------- Word Count ----------\n")  # Print the title of the program

    num_words = get_num_words(book_text)  # Call the function to count words in the book
    print(f'Found {num_words} total words\n')  # Print the content of the book file

    character_count = count_characters(book_text)  # Call the function to count characters in the book
    print(f"----------- Character Count ----------\n")
    list_of_dicts = report(character_count)  # Call the function to report character counts
    for dictionary in list_of_dicts:
        key = list(dictionary.keys())[0]
        if key.isalpha():
            print(f"{key}: {dictionary[key]}")
    print(f"============= END ===============")  # Print the end of the document

main()
# This code reads the content of a book file and prints it to the console.