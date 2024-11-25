from Crypto.Cipher import AES, DES
import base64
import hashlib

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = plain_text + (8 - len(plain_text) % 8) * chr(8 - len(plain_text) % 8)
    ciphertext = cipher.encrypt(padded_text.encode())
    return base64.b64encode(ciphertext).decode()

def base64_encrypt(plain_text):
    return base64.b64encode(plain_text.encode()).decode()

def caesar_encrypt(plain_text, shift=3):
    encrypted = ''.join(
        chr((ord(char) + shift - 65) % 26 + 65) if char.isupper() else
        chr((ord(char) + shift - 97) % 26 + 97) if char.islower() else char
        for char in plain_text
    )
    return encrypted

def generate_method_hash(method_1, method_2):
    return hashlib.sha256(f"{method_1}-{method_2}".encode()).hexdigest()

def encrypt():
    print("--- Encryption Process ---")
    text_to_encrypt = input("Enter the text to encrypt: ")

    print("Select the first encryption method:")
    print("1. AES")
    print("2. DES")
    print("3. Base64")
    print("4. Caesar")
    method_1 = input("Enter your choice (1/2/3/4): ")

    print("Select the second encryption method:")
    print("1. AES")
    print("2. DES")
    print("3. Base64")
    print("4. Caesar")
    method_2 = input("Enter your choice (1/2/3/4): ")

    aes_key = b'1234567890123456'
    des_key = b'12345678'

    encrypted_text = text_to_encrypt
    if method_1 == '1':
        encrypted_text = aes_encrypt(encrypted_text, aes_key)
    elif method_1 == '2':
        encrypted_text = des_encrypt(encrypted_text, des_key)
    elif method_1 == '3':
        encrypted_text = base64_encrypt(encrypted_text)
    elif method_1 == '4':
        encrypted_text = caesar_encrypt(encrypted_text)

    if method_2 == '1':
        encrypted_text = aes_encrypt(encrypted_text, aes_key)
    elif method_2 == '2':
        encrypted_text = des_encrypt(encrypted_text, des_key)
    elif method_2 == '3':
        encrypted_text = base64_encrypt(encrypted_text)
    elif method_2 == '4':
        encrypted_text = caesar_encrypt(encrypted_text)

    method_hash = generate_method_hash(method_1, method_2)

    print(f"Encrypted Text: {encrypted_text}")
    print(f"Method Hash: {method_hash}")
