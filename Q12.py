def sum_of_digits(number):
    # Convert number to absolute value to handle negative numbers
    number = abs(number)
    # Initialize sum variable
    digit_sum = 0

    # Iterate through each digit in the number
    while number > 0:
        # Add the last digit to the sum
        digit_sum += number % 10
        # Remove the last digit from the number
        number //= 10

    return digit_sum


# Example usage
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("The sum of the digits of {} is {}.".format(number, result))

