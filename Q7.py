def get_string_length():
    user_input = input("Enter a string: ")
    length = len(user_input)
    return length

# Example usage
length = get_string_length()
print("The length of the entered string is {}.".format(length))
