def get_num_words(book): 
    num_words = book.split()  # Split the content into words
    words = len(num_words)  # Count the number of words
    return words  # Return the word count

def count_characters(book):
    lowercase = book.lower()  # Convert the content to lowercase
    dictionary = {}  # Initialize an empty dictionary to store character counts

    for char in lowercase:  # Iterate through each character in the content
        if char.isalpha():  # Check if the character is an alphabetic letter
            if char in dictionary:  # If the character is already in the dictionary
                dictionary[char] += 1  # Increment its count
            else:
                dictionary[char] = 1  # Initialize its count to 1
    return dictionary  # Return the dictionary of character counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries

def report(dictionary):
    """
    This function takes a dictionary of character counts and prints the results.
    """
    list_of_dicts = []
    for key, value in dictionary.items():  # Iterate through each character in the dictionary
        list_of_dicts.append({key: value})  # Append the character and its count to the list
    list_of_dicts.sort(key=lambda x: list(x.values())[0], reverse=True)  # Sort the list of dictionaries by count in descending order
    return list_of_dicts  # Return the sorted list of dictionaries
