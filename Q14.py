def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (empty line to stop): ")
        if line == "":
            break
        lines.append(line)

    return lines


# Example usage
print("Enter multiple lines. Press Enter without typing anything to stop.")
entered_lines = read_multiple_lines()

print("\nEntered lines:")
for line in entered_lines:
    print(line)
