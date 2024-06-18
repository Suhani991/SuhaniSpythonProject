def string_to_list(input_string):
    char_list = list(input_string)
    return char_list


# Example usage
try:
    input_string = input("Enter a string: ")

    char_list = string_to_list(input_string)

    print("Original string:", input_string)
    print("List of characters:", char_list)

except Exception as e:
    print(f"Error: {e}")
