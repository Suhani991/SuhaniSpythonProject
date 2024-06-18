def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# Example usage
main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if check_substring(main_string, substring):
    print("The substring '{}' is present in the main string.".format(substring))
else:
    print("The substring '{}' is not present in the main string.".format(substring))
