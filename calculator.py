# Simple CLI Calculator

print("Simple Calculator")
print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user input
choice = input("Enter choice (1/2/3/4): ")

# Take two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation using if-else
if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")

else:
    print("Invalid input")

