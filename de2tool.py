import os
from encryption import encrypt  # Import encrypt function from encrypt.py
from decryption import decrypt  # Import decrypt function from decrypt.py
import pyfiglet  # To generate ASCII art text
from termcolor import colored  # To add color to the text

def print_banner():
    """Print a big and stylish banner for DE2Tool."""
    # Generate big ASCII text for the banner using pyfiglet with a larger width
    banner = pyfiglet.figlet_format("DE2Tool", width=1000)  # Increase the width for a larger banner
    
    # Alternatively, you can try different fonts like "slant", "block", "big", etc.
    # banner = pyfiglet.figlet_format("DE2Tool", font="block", width=200)
    
    # Color the banner using termcolor (red color in this case)
    colored_banner = colored(banner, 'red')
    
    # Print the colored banner
    print(colored_banner)

def main():
    print_banner()  # Print the big, stylish banner
    while True:
        print("Choose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            encrypt()  # Calls the encryption function from encrypt.py
        elif choice == '2':
            decrypt()  # Calls the decryption function from decrypt.py
        elif choice == '3':
            print("Exiting the tool. Goodbye!")  # Exit message
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid choices

if __name__ == "__main__":
    main()  # Start the program
