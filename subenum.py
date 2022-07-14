#!/usr/bin/python3
#Use Unix OS on Sudo UID, for best experience use Kali Linux!

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

