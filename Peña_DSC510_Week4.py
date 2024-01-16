# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Miles Peña
# 9/23/2023

def calculated_cost(feet_required, cost):
    total_cost = feet_required * cost
    return total_cost


def main():
    name = input("Enter name: ")
    print("Welcome", name)
    company_name = input("Please enter company name: ")
    try:
        feet_required = int(input("Please enter number of feet of fiber optic cable required to be installed: "))
        # Convert to integer for mathematics purposes
    except ValueError:
        print("You didn't enter a valid number!")
    else:
        # Compute if statements for all required executions
        if 100 < feet_required <= 250:
            cost = 0.80
        elif 250 < feet_required <= 500:
            cost = 0.70
        elif feet_required > 500:
            cost = 0.50
        else:
            cost = 0.87

    total_cost = calculated_cost(feet_required, cost)
    print("Fiber Optic Cable Cost")
    print("Company name: ", company_name)
    print("Feet of fiber optic cable required: ", feet_required)
    print("Calculated cost: $", format(total_cost, ",.2f"))


if __name__ == "__main__":
    main()
