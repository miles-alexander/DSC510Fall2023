# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Miles Peña
# 11/03/2023

import requests


def get_fact():
    url = "https://catfact.ninja/fact"
    response = requests.request("GET", url)
    fact = response.json()["fact"]
    print(fact)


def main():
    print("Welcome to Random Facts About Cats!")
    while True:
        try:
            answer = input("Would You Like to Learn a Random Fact? Type Y for Yes or any other key to exit: ")
            if answer.lower() == "y":
                print("Here is Your Random Cat Fact: ")
                get_fact()
                while True:
                    second_answer = input("Would You Like to Learn Another? Type Y for Yes or any other key to exit: ")
                    if second_answer.lower() == "y":
                        print("Here is Your Next Random Cat Fact: ")
                        get_fact()
                    else:
                        break
            else:
                print("Thank you for using my program!")
                break
        except requests.exceptions.HTTPError as error:
            print(error)
            break
        except requests.URLRequired as error:
            print(error)
            break
        except requests.ConnectionError as error:
            print(error)
            break


if __name__ == "__main__":
    main()
