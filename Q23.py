def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Example usage
try:
    choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ").upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F.")

    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C.")

    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

except ValueError:
    print("Error: Please enter a valid number for temperature.")
