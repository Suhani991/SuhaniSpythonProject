def find_min_max(numbers):
    if not numbers:
        return None, None  # Return None for both min and max if list is empty

    min_value = min(numbers)
    max_value = max(numbers)

    return min_value, max_value


# Example usage
try:
    # Input list from the user
    input_list = input("Enter elements of the list separated by spaces: ").split()

    # Convert input list elements to integers
    numbers = list(map(int, input_list))

    # Find minimum and maximum values in the list
    min_value, max_value = find_min_max(numbers)

    # Output the result
    print("Minimum value:", min_value)
    print("Maximum value:", max_value)

except ValueError:
    print("Error: Please enter valid numbers separated by spaces.")
