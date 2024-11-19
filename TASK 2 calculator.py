import math

# Function to perform basic arithmetic operations
def basic_operations():
    print("\nBasic Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    choice = input("Choose an operation (1-4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Function to perform advanced operations
def advanced_operations():
    print("\nAdvanced Operations:")
    print("1. Square Root")
    print("2. Power (x^y)")
    print("3. Logarithm (log10)")
    print("4. Sine (sin)")
    print("5. Cosine (cos)")
    print("6. Tangent (tan)")
    choice = input("Choose an operation (1-6): ")

    try:
        if choice == '1':
            num = float(input("Enter a number: "))
            if num >= 0:
                print(f"Result: √{num} = {math.sqrt(num)}")
            else:
                print("Error: Square root of a negative number is not defined!")
        elif choice == '2':
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print(f"Result: {base}^{exp} = {math.pow(base, exp)}")
        elif choice == '3':
            num = float(input("Enter a number: "))
            if num > 0:
                print(f"Result: log10({num}) = {math.log10(num)}")
            else:
                print("Error: Logarithm is not defined for non-positive numbers!")
        elif choice in ['4', '5', '6']:
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)
            if choice == '4':
                print(f"Result: sin({angle}°) = {math.sin(radians)}")
            elif choice == '5':
                print(f"Result: cos({angle}°) = {math.cos(radians)}")
            elif choice == '6':
                print(f"Result: tan({angle}°) = {math.tan(radians)}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Function to handle the main menu
def calculator_menu():
    while True:
        print("\n--- Python Calculator ---")
        print("1. Basic Operations")
        print("2. Advanced Operations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            basic_operations()
        elif choice == '2':
            advanced_operations()
        elif choice == '3':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the calculator
if __name__ == "__main__":
    calculator_menu()
