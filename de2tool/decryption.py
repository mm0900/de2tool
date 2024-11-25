from Crypto.Cipher import AES, DES
import base64
import hashlib
from encryption import generate_method_hash

def aes_decrypt(cipher_text, key):
    cipher_bytes = base64.b64decode(cipher_text)
    nonce, tag, ciphertext = cipher_bytes[:16], cipher_bytes[16:32], cipher_bytes[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

def des_decrypt(cipher_text, key):
    cipher_bytes = base64.b64decode(cipher_text)
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = cipher.decrypt(cipher_bytes).decode()
    padding_length = ord(padded_text[-1])
    return padded_text[:-padding_length]

def caesar_decrypt(cipher_text, shift=3):
    decrypted = ''.join(
        chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else
        chr((ord(char) - shift - 97) % 26 + 97) if char.islower() else char
        for char in cipher_text
    )
    return decrypted

def determine_methods_from_hash(method_hash):
    for method_1 in ['AES', 'DES', 'Base64', 'Caesar']:
        for method_2 in ['AES', 'DES', 'Base64', 'Caesar']:
            if generate_method_hash(str(['AES', 'DES', 'Base64', 'Caesar'].index(method_1) + 1), 
                                        str(['AES', 'DES', 'Base64', 'Caesar'].index(method_2) + 1)) == method_hash:
                return method_1, method_2
    return None, None

def decrypt():
    print("--- Decryption Process ---")
    text_to_decrypt = input("Enter the text to decrypt: ")
    method_hash = input("Enter the methods hash: ")

    method_1, method_2 = determine_methods_from_hash(method_hash)

    if not method_1 or not method_2:
        print("Unknown method hash.")
        return

    aes_key = b'1234567890123456'
    des_key = b'12345678'

    decrypted_text = text_to_decrypt
    if method_2 == 'AES':
        decrypted_text = aes_decrypt(decrypted_text, aes_key)
    elif method_2 == 'DES':
        decrypted_text = des_decrypt(decrypted_text, des_key)
    elif method_2 == 'Base64':
        decrypted_text = base64.b64decode(decrypted_text).decode()
    elif method_2 == 'Caesar':
        decrypted_text = caesar_decrypt(decrypted_text)

    if method_1 == 'AES':
        decrypted_text = aes_decrypt(decrypted_text, aes_key)
    elif method_1 == 'DES':
        decrypted_text = des_decrypt(decrypted_text, des_key)
    elif method_1 == 'Base64':
        decrypted_text = base64.b64decode(decrypted_text).decode()
    elif method_1 == 'Caesar':
        decrypted_text = caesar_decrypt(decrypted_text)

    print(f"Decrypted Text: {decrypted_text}")
