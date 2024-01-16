# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Miles Peña
# 9/17/2023

def main():
    name = input("Enter name: ")

    print("Welcome", name)
    company_name = input("Please enter company name: ")

    feet_required = int(input("Please enter number of feet of fiber optic cable required to be installed: "))
    # Convert to integer for mathematics purposes

    # Compute the calculated cost of inputted number of feet of cable at $0.87 a foot
    # Compute if statements for all required executions

    if 100 < feet_required <= 250:
        cost = 0.80
    elif 250 < feet_required <= 500:
        cost = 0.70
    elif feet_required > 500:
        cost = 0.50
    else:
        cost = 0.87
    total_cost = feet_required * cost
    print("Fiber Optic Cable Cost")

    print("Company name: ", company_name)
    print("Feet of fiber optic cable required: ", feet_required)
    print("Calculated cost: ", total_cost)


if __name__ == "__main__":
    main()
