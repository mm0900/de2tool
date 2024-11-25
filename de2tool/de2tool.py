import os
from encryption import encrypt
from decryption import decrypt
import pyfiglet
from termcolor import colored

def print_banner():
    banner = pyfiglet.figlet_format("DE2Tool", width=1000)
    colored_banner = colored(banner, 'red')
    print(colored_banner)

def main():
    print_banner()
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            encrypt()
        elif choice == '2':
            decrypt()
        elif choice == '3':
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
