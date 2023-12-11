#!/usr/bin/python3
"""Pycodestyle check"""


def greet_user(name):
    """This will greet the user."""
    print(f"Hello, {name.title()}!")


def cal_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b


def main1():
    """This is our main function"""
    name = input("Enter your name: ")
    greet_user(name)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = cal_sum(num1, num2)

    print(f"The sum of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main1()

