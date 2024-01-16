# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Miles Peña
# 10/2/2023

def main():
    temperatures = []  # Set empty list for variable temperatures
    print("Enter temperatures one by one or enter 'Q' to quit: ")

    while True:
        try:
            temp = input()  # Allow user input of temperatures
            if temp.lower() == 'q':  # Not case-sensitive
                print("Thank you for using my program!")
                break  # Break for sentinel value
            temperatures.append(float(temp))
        except ValueError:
            print("Please enter a valid temperature or 'Q' to quit")
    print("The largest temperature in the list is: ", max(temperatures))
    print("The smallest temperature in the list is: ", min(temperatures))
    print("The total number of temperatures in the list is: ", len(temperatures))


if __name__ == "__main__":
    main()
