#!/bin/python3

print("Made By - ")
print(''' 
░█████╗░░█████╗░██████╗░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║╚════██║
███████║███████║██████╔╝██║░░███╔═╝
██╔══██║██╔══██║██╔══██╗██║██╔══╝░░
██║░░██║██║░░██║██║░░██║██║███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝ ''')

print("\n")
operators = input("Choose a operator( + | - | * | / | % | ** ) : ")
first_number = input("Enter first number : ")
second_number = input("Enter second number : ")

first_number = int(first_number)
second_number = int(second_number)

if operators == "+":
    print("The sum is : ")
    print(first_number + second_number)

elif operators == "-":
    print("The difference is : ")
    print(first_number - second_number)

elif operators == "*":
    print("The multiplication is : ")
    print(first_number * second_number)

elif operators == "/":
    print("The division is : ")
    print(first_number / second_number)

elif operators == "**":
    print("The solution of exponent is : ")
    print(first_number ** second_number)

elif operators == "%":
    print("The modulus is : ")
    print(first_number % second_number)

else:
    print("Try again later!")
# ----------------------------------------------------------->End of Code!



