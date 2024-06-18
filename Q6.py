def read_from_file():
    filename = "output.txt"

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print("The file {} does not exist.".format(filename))


# Call the function to execute the reading process
read_from_file()
