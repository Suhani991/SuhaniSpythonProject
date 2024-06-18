def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator!"

# Example usage
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print(f"Error: {e}")
