# test_de2tool.py

from encryption import encrypt
from decryption import decrypt

def test_encrypt_decrypt():
    text = "Hello, DE2Tool!"
    key = "mysecurekey12345"
    algorithm = "AES"

    
    encrypted_text = encrypt(text, key, algorithm)
    decrypted_text = decrypt(encrypted_text, key, algorithm)
    assert decrypted_text == text
