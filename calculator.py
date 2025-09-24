# calculator.py
import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_logarithm(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

if __name__ == "__main__":
    print("Scientific Calculator")
    while True:
        print("\nChoose an operation:")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter number: "))
                if choice == '1':
                    print("Result:", square_root(num1))
                elif choice == '2':
                    if num1 < 0:
                        print("Factorial is not defined for negative numbers.")
                    else:
                        print("Result:", factorial(int(num1)))
                elif choice == '3':
                    print("Result:", natural_logarithm(num1))
                elif choice == '4':
                    num2 = float(input("Enter exponent: "))
                    print("Result:", power(num1, num2))
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            break
        else:
            print("Invalid input")