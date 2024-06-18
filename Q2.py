def check_even_or_odd(number):
    if number % 2 == 0:
        return "The number {} is even.".format(number)
    else:
        return "The number {} is odd.".format(number)

# Example usage
number = int(input("Enter a number: "))
result = check_even_or_odd(number)
print(result)
