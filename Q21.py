def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


# Example usage
try:
    # Input list from the user
    input_list = input("Enter elements of the list separated by spaces: ").split()

    # Convert input list elements to integers
    lst = list(map(int, input_list))

    # Input element to count its occurrences
    element = int(input("Enter the element to count its occurrences: "))

    # Count occurrences of the element in the list
    occurrences = count_occurrences(lst, element)

    # Output the result
    print("Occurrences of", element, "in the list:", occurrences)

except ValueError:
    print("Error: Please enter valid numbers separated by spaces.")
