def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum


# Example usage
try:
    # Prompt the user to enter numbers separated by spaces
    input_numbers = input("Enter numbers separated by spaces: ")

    # Convert input string to a list of integers
    numbers = list(map(int, input_numbers.split()))

    # Calculate the sum of numbers
    result = calculate_sum(numbers)

    # Print the result
    print("Sum of the numbers:", result)

except ValueError:
    print("Error: Please enter valid numbers separated by spaces.")
