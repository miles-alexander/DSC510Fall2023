# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Miles Peña
# 9/30/2023

def perform_calculation(operation):
    print("Perform Calculation")
    first_value = float(input("Please provide your first number: "))
    second_value = float(input("Please provide your second number: "))
    # Ensure values are represented as floats to allow decimals as input

    if operation == '+':
        calculated_value = first_value + second_value
    elif operation == '-':
        calculated_value = first_value - second_value
    elif operation == '*':
        calculated_value = first_value * second_value
    elif operation == '/':
        if second_value == 0:
            print("Cannot divide by zero.")
        else:
            calculated_value = first_value / second_value
    else:
        print("Please enter a valid number!")

    print("The calculated value is :", calculated_value)


def calculate_average():
    numbers_to_input = int(input("How many numbers would you like to input: "))
    total = 0

    for inputs in range(numbers_to_input):
        number_to_average = int(input("Enter number: "))
        total = total + number_to_average
        print("Total:", total)
        print("Average:", total / numbers_to_input)


def main():
    while True:
        print("What operation would you like to perform?")
        print("Please enter '+' for addition.")
        print("Please enter '-' for subtraction.")
        print("Please enter '*' for multiplication.")
        print("Please enter '/' for division.")
        print("Please enter 'a' or 'A' for average.")
        break

    operation = input("Please select an operation: ")
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        perform_calculation(operation)
    elif operation == 'a' or 'A':
        calculate_average()
    else:
        print("Invalid operation. Please try again with a valid operation.")


if __name__ == "__main__":
    main()
