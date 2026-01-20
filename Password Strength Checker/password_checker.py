#!/usr/bin/env python3

import string
import signal
import sys
import os
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n\nExiting the script...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

reqs = string.ascii_letters + string.punctuation

def main():

    while True:

        print("Password Checker")

        print("\nRequirements => Uppercase/Lowercase letters, Min. Length = 8, min. a special character\n")

        password = input("\tInput your password: ")
        if any(letter in reqs for letter in password) and len(password) >= 8:
            print(colored("\n\t[+] Password is acceptable!\n", 'green'))
            break
        else:
            print(colored("\n\t[+] Password is too weak!\n", 'red'))
            input("Please, press <Enter> to try again...")
            os.system("clear")
            
if __name__ == '__main__':
    os.system("clear")
    main()

# ~ jordi 志
