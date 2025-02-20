# Python Dilinde Hesap Makinesi
# Calculator in Python Language

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter your choice (1/2/3/4): ")

while operation not in ["1", "2", "3", "4"]:
    operation = input("Please enter a valid choice (1/2/3/4): ")

if operation == "1":
    result = first_number + second_number
    print(f"Result: {first_number} + {second_number} = {result}")

elif operation == "2":
    result = first_number - second_number
    print(f"Result: {first_number} - {second_number} = {result}")

elif operation == "3":
    result = first_number * second_number
    print(f"Result: {first_number} * {second_number} = {result}")

elif operation == "4":
    if second_number == 0:
        print("Result: Undefined (division by zero)")
    else:
        result = first_number / second_number
        print(f"Result: {first_number} / {second_number} = {result}")

print("HAVE A GOOD DAY!!")

# son
# the end
