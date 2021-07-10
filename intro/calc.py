# description
"""
Script: Simple calculator
Author: Reese Gick
Year: 2021
Functionality: Basic math
"""


# imports 


# globals 


# functions

def print_menu():
    print("-" * 30)
    print("  PyCalc")
    print("-" * 30)

    print("[1] - Sum")
    print("[2] - Subtract")
    print("[3] - Multiplication")
    print("[4] - Division")

    print("[5] - Is it even?")

    print("[q] - Quit")

# instructions

selected_option = ""
while(selected_option !="q"):
    print_menu()
    selected_option = input("Please select an option: ")

    num1 = float(input("Provide num 1:"))
    num2 = float(input("Provide num 2:"))


    if(selected_option=="1"):
        result = float(num1) + float(num2)
        print(result)

    elif (selected_option == "2"):
        result = num1 - num2
        print(result)


    elif (selected_option == "3"):
        result = num1 * num2
        print(result)

    elif (selected_option == "4"):
        print("invalid,please try again")
        result = num1 / num2
        print(result)

    elif (selected_option == "5"):
        result = num1 
        ("if (num % 2) == 0)  
        print("{0} is Even number".format(num))  
        else:  
        print("{0} is Odd number".format(num))  ")
        

print("Good bye!")