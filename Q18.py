def are_anagrams(string1, string2):
    # Remove spaces and convert to lowercase for case insensitivity
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # Check if the lengths are different
    if len(string1) != len(string2):
        return False

    # Count frequency of each character in both strings
    char_count1 = {}
    char_count2 = {}

    for char in string1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in string2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Compare the character counts
    return char_count1 == char_count2


# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The strings '{}' and '{}' are anagrams.".format(string1, string2))
else:
    print("The strings '{}' and '{}' are not anagrams.".format(string1, string2))
