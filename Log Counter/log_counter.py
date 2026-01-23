#!/usr/bin/env python3

import re
import sys
import signal
import time
import os
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n\n[!] Exiting the script...\n", 'red'))
    sys.exit(1)

def clear():
    if os.name == 'posix':
        os.system("clear")
    elif os.name == 'nt':
        os.system("cls")
    else:
        print(colored("[!] OS not supported!", 'red'))

signal.signal(signal.SIGINT, def_handler)

def main():
    clear()
    ip_counts = {}

    print("Log IP Counter\n")

    while True:
        try:
            print("'Ctrl+C to exit script'")
            file_to_scan = input("\n[+] File to scan: ")

            with open(file_to_scan, 'r') as f:
                for line in f:
                    ip_addr = re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line)

                    if not ip_addr:
                        continue

                    ip_addr = ip_addr[0]

                    if ip_addr in ip_counts:
                        ip_counts[ip_addr] += 1
                    else:
                        ip_counts[ip_addr] = 1

            break  

        except FileNotFoundError:
            print(colored("\n[!] File does not exist!\n", 'red'))
            time.sleep(1)

    clear()
    print("\nRepeated IPs:\n")
    for ip, count in ip_counts.items():
        if count > 1:
            print(colored(ip, 'green') + " appeared " + colored(count, 'red') + " times""\n")


if __name__ == '__main__':
    main()
