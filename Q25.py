def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as src:
            # Read the entire content of the source file
            content = src.read()

        # Open the destination file for writing
        with open(destination_file, 'w') as dest:
            # Write the content read from the source file to the destination file
            dest.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")

    except FileNotFoundError:
        print("Error: One or both files not found.")

    except IOError as e:
        print(f"Error: {e}")


# Example usage
try:
    source_file = input("Enter the source file path: ")
    destination_file = input("Enter the destination file path: ")

    copy_file(source_file, destination_file)

except Exception as e:
    print(f"Error: {e}")
