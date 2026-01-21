#!/usr/bin/env python3

import signal
import sys
import os
import time
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n\n[!] Exiting the script...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Agenda:
        def __init__(self):
            self.contact_list = {}

        def add_contact(self, name, number):
            self.contact_list[name] = number
            print(colored(f"\n[+] Contact successfully added to the agenda!\n", 'green'))

        def delete_contact(self, name):
            if name in self.contact_list:
                del self.contact_list[name]
                print(colored(f"\n[+] Contact {name} successfully deleted from the agenda!\n", 'green'))
            else:
                print(colored(f"\n[-] Contact not found!", 'red'))

        def search_contact(self, prompt):
            for key, value in self.contact_list.items():
                if key == prompt or value == prompt:
                    print(colored(f"[+] Contact {prompt} was found successfully!", 'green'))
                    print(f"\n[Name]: {key}")
                    print(f"[Number]: {value}\n")
                    return
                elif key != prompt or value != prompt:
                    pass
                else:
                    print(colored("[-] Contact not found\n", 'red'))

        def show_agenda(self):
            for name, number in self.contact_list.items():
                print(f"\n[Name]: {name}")
                print(f"[Number]: {number}\n")

def main():
    agenda = Agenda()

    while True:
        os.system("clear")
        print("Contact Manager")
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Show Agenda")
        print("5. Exit")

        choice = int(input("\nPick an option: "))

        if choice == 1:
            name = input("\nWhat is the name of your new contact?: ")
            number = int(input("What is the phone number of your new contact?: "))

            agenda.add_contact(name, number)
            input("\nPress <Enter> to continue...")

        elif choice == 2:
            name = input("\nWhat is the name of the contact you wish to delete?: ")

            agenda.delete_contact(name)
            input("\nPress <Enter> to continue...")

        elif choice == 3:
            prompt = input("\nContact to look for?: ")

            agenda.search_contact(prompt)
            input("\nPress <Enter> to continue...")

        elif choice == 4:
            os.system("clear")
            print("Contact List:")
            
            agenda.show_agenda()
            input("\nPress <Enter> to continue...")

        elif choice == 5:
            print("\nFarewell!\n")
            break
        else:
            print(colored("\n[!] Input selected is not valid! Please try again...", 'red'))
            time.sleep(2)
    
if __name__ == '__main__':
    main()

# ~ jordi 志
