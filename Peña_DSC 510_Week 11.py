# DSC 510
# Week 11
# Programming Assignment Week 11
# Author Miles Peña
# 11/11/2023

import locale


class CashRegister:

    def __init__(self):
        self.item = 0
        self.total = 0.0

    def add_item(self, price):
        self.item += 1
        self.total += price

    def get_total(self):
        return self.total

    def get_count(self):
        return self.item

    def clear_cart(self):
        self.item = 0
        self.total = 0.0


def main():
    print("Welcome to the Cash Register!")
    register = CashRegister()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    while True:
        choice = input("Enter the letter a to add item to the cart, or q to quit the program: ")
        if choice.lower() == 'a':
            price = float(input("Enter the price of the item: "))
            register.add_item(price)
        elif choice.lower() == 'q':
            break
        else:
            print("Please enter a valid letter!")

    print("The total number of items in your cart is: ", register.get_count())
    print("The total price of the items in the cart is: ", locale.currency(register.get_total()))


if __name__ == '__main__':
    main()
