#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/2/2023
# This program allows for user to choose 2 numbers
# and a mathematical sign that will be used in the calculation.
# It will then add/subtract/divide/multiply/modulo of your 2 numbers.


# Function that checks what sign will be used in the calculation.
def calculator(sign, first_number, second_number):
    if sign == "+":
        answer = first_number + second_number
    elif sign == "-":
        answer = first_number - second_number
    elif sign == "*":
        answer = first_number * second_number
    elif sign == "/":
        answer = first_number / second_number
    elif sign == "%":
        answer = first_number % second_number
    return answer


def main():
    # Getting user input for number1
    first_number = input("Enter your first number as a decimal: ")

    # Getting user input for number2
    second_number = input("Enter your second number as a decimal: ")

    # Getting user input for mathematical sign.
    sign = input("Enter a mathematical sign (+,-,*,/,%):")

    # Using if statement to check if mathematical sign is valid.
    # If it is valid then their numbers will be converted into decimals and error check using a try catch.
    if sign == "+" or sign == "-" or sign == "*" or sign == "/" or sign == "%":
        # Using a try catch to catch any errors.
        # Convert number1 and number2 into decimals.
        try:
            first_number_as_float = float(first_number)
            second_number_as_float = float(second_number)

            # Calling calculator() function.
            answer = calculator(sign, first_number_as_float, second_number_as_float)

            # Displaying the answer to the user.
            print(
                "{} {} {} = {}".format(
                    first_number_as_float, sign, second_number_as_float, answer
                )
            )

        # Catching any errors.
        except:
            print("Invalid number.")
    # Using else statement, to display an error message when the mathematical sign is invalid.
    else:
        print("{} is an invalid mathematical sign.".format(sign))


if __name__ == "__main__":
    main()
