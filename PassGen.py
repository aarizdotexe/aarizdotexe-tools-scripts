#!/bin/python3
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '89']

print("Welcome to Python Password Gen V1.1\n")
print("Made By - ")
print(''' 
░█████╗░░█████╗░██████╗░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║╚════██║
███████║███████║██████╔╝██║░░███╔═╝
██╔══██║██╔══██║██╔══██╗██║██╔══╝░░
██║░░██║██║░░██║██║░░██║██║███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝ \n''')
print("Recommendations - \n1.Make your password atleast of 18 characters.\n2.Use different password for different accounts.\n3.Use Password Generators and Password Vaults/Managers for better storage of passwords.\n\nStart Here!\n")

in_letter = int(input("Number of letters(Recommended 8+): "))
in_sym = int(input("Number of symbols(Recommended 2+): "))
in_num = int(input("Number of numeric characters(Recommended 4+): "))

pass_list = []
for char in range(1, in_letter + 1):
    pass_list.append(random.choice(letters))
for char in range(1, in_sym + 1):
    pass_list += random.choice(symbols)
for char in range(1, in_num + 1):
    pass_list += random.choice(numbers)

# Convert List to String here!
password = ""
for char in pass_list:
    password += char
print(password)
