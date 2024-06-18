def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count of character in the dictionary
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

# Example usage
input_string = input("Enter a string: ")
frequency = count_character_frequency(input_string)

print("Character frequencies:")
for char, freq in frequency.items():
    print(f"Character '{char}' occurs {freq} times")
