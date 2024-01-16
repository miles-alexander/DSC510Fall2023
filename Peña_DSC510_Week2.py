# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Miles Peña
# 9/8/2023

name = input("Enter name: ")

print("Welcome", name)
company_name = input("Please enter company name: ")

feet_required = int(input("Please enter number of feet of fiber optic cable required: "))
# Convert to integer for mathematics purposes

cost = (feet_required * 0.87)  # Compute the calculated cost of 5 feet of cable at $0.87 a foot


print("Fiber Optic Cable Cost")

print("Company name: ", company_name)
print("Feet of fiber optic cable required: ", feet_required)
print("Calculated cost: ", cost)



