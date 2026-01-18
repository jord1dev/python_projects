#!/usr/bin/env python3

import random
import signal
import sys
import os
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n\nExiting the script...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def game():

    os.system("clear")

    max_range = int(input("\nInput the max. number to guess from range?: "))

    unknown_number = random.randint(1, max_range)

    try:
   
        number_picked = int(input(f"\nGuess a number from 1 to {max_range}: "))

        if number_picked == unknown_number:
            print(colored(f"\n[+] Nice! Number {number_picked} was the right number!\n", 'green'))
        elif number_picked > max_range:
            print(colored(f"\n[!] Number selected is not in the specified range!\n", 'red'))
        else:
            print(colored(f"\n[-] Number {number_picked} was not the right number!\n", 'red'))
    except ValueError:
        print(colored("\n[!] Not a valid input!\n", 'red'))

def main():
    game()
    

if __name__ == '__main__':
    main()

# ~ jordi 志
