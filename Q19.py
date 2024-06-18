import string


def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)

    # Use translate() method to remove punctuation
    clean_string = input_string.translate(translator)

    return clean_string


# Example usage
input_string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:", cleaned_string)
