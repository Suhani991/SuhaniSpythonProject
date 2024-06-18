def write_to_file():
    # Prompt the user for input
    user_input = input("Enter a string: ")

    # Define the filename
    filename = "output.txt"

    # Open the file in write mode and write the user input to it
    with open(filename, "w") as file:
        file.write(user_input)

    print(f"The string has been written to {filename}")


# Call the function to write the user's input to a file
write_to_file()
