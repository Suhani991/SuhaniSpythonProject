def generate_fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence


# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
result = generate_fibonacci(n)
print("The first {} numbers in the Fibonacci sequence are: {}".format(n, result))
