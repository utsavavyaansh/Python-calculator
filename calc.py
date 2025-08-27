# Python Advanced Calculator
# Author: Utsav Avyaansh

import math

def calculator():
    print("===== Python Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y)")
    print("7. Square Root (√)")
    print("8. Exit")

    while True:
        choice = input("\nEnter choice (1-8): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a + b)

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a - b)

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", a * b)

        elif choice == '4':
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            if b == 0:
                print("Error: Division by zero is not allowed!")
            else:
                print("Result:", a / b)

        elif choice == '5':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Result:", a % b)

        elif choice == '6':
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", math.pow(a, b))

        elif choice == '7':
            a = float(input("Enter number: "))
            if a < 0:
                print("Error: Square root of negative number not defined!")
            else:
                print("Result:", math.sqrt(a))

        elif choice == '8':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1-8.")

# Run the calculator
if __name__ == "__main__":
    calculator()
