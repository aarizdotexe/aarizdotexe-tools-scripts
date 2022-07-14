#!/usr/bin/python3

import subprocess

cmd1 = subprocess.call(['apt', 'install', 'amass']) 

print("\n")
print("Made By - ")
print(''' 
░█████╗░░█████╗░██████╗░██╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║╚════██║
███████║███████║██████╔╝██║░░███╔═╝
██╔══██║██╔══██║██╔══██╗██║██╔══╝░░
██║░░██║██║░░██║██║░░██║██║███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝ ''')

link = input("[+] Website/IP to Scan: ")

cmd = subprocess.call(['amass', 'enum', '-d', link])

