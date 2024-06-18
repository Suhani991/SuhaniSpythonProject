def convert_to_title_case(input_string):
    # Split the input string into words
    words = input_string.split()

    # Initialize an empty list to store capitalized words
    title_case_words = []

    # Iterate through each word and capitalize the first letter
    for word in words:
        capitalized_word = word.capitalize()
        title_case_words.append(capitalized_word)

    # Join the capitalized words back into a single string
    title_case_string = ' '.join(title_case_words)

    return title_case_string


# Example usage
input_string = input("Enter a string: ")
title_case_string = convert_to_title_case(input_string)
print("String in title case:", title_case_string)
