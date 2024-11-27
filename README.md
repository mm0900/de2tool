# DE2Tool
![Logo](./"C:\Users\akhil\OneDrive\Desktop\de2tool\logo.png")

## Description
DE2Tool is a versatile encryption and decryption tool designed to help users securely handle sensitive data. The tool supports multiple encryption algorithms, including AES, DES, Base64, and Caesar Cipher. This project allows you to encrypt and decrypt text using combinations of these methods for added security.

## Features
- **AES Encryption**: Advanced encryption standard for secure encryption.
- **DES Encryption**: Data encryption standard for symmetric key encryption.
- **Base64 Encoding**: Encode data into Base64 format.
- **Caesar Cipher**: Simple cipher shifting characters by a specified number.

## Prerequisites
Before running DE2Tool, ensure you have Python installed on your system. You will also need to install the required Python libraries listed in the `requirements.txt`.

## How to Use

### Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/mm0900/de2tool.git
```
### Install Dependencies
Navigate to the project directory:
```bash
cd de2tool
```
### Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
This command will install the necessary libraries specified in requirements.txt, including dependencies like pycryptodome, pyfiglet, and termcolor.

### Example Workflow
Select the encryption method you want to use (AES, DES, Base64, or Caesar Cipher).
Enter the text you wish to encrypt.
The tool will display the encrypted text and the method hash.
To decrypt, provide the encrypted text and the method hash.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
