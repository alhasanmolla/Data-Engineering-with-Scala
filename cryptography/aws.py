import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import os
import sys

# Load sensitive information from environment variables
key = os.getenv("ENCRYPTION_KEY", "default_key")  # Replace with actual environment variable
iv = os.getenv("ENCRYPTION_IV", "default_iv")
salt = os.getenv("ENCRYPTION_SALT", "default_salt")
aws_access_key = os.getenv("AWS_ACCESS_KEY", "default_access_key")
aws_secret_key = os.getenv("AWS_SECRET_KEY", "default_secret_key")

# Error handling for missing configuration
if not (key and iv and salt):
    print("Error: Missing encryption configuration (key, IV, or salt).")
    sys.exit(1)

if not (aws_access_key and aws_secret_key):
    print("Error: Missing AWS credentials.")
    sys.exit(1)

# Constants for AES
BS = 16  # Block size for AES
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]

def get_private_key():
    """Derive a private key using PBKDF2."""
    Salt = salt.encode('utf-8')
    kdf = PBKDF2(key, Salt, 64, 1000)
    key32 = kdf[:32]
    return key32

def encrypt(raw):
    """Encrypt plaintext using AES."""
    raw = pad(raw)
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return base64.b64encode(cipher.encrypt(raw)).decode('utf-8')

def decrypt(enc):
    """Decrypt ciphertext using AES."""
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf-8')

# Example usage of encryption
try:
    plaintext = "ALHASAN"
    encrypted_text = encrypt(plaintext)
    decrypted_text = decrypt(encrypted_text)

    print("Original Text:", plaintext)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)
except Exception as e:
    print(f"Encryption/Decryption Error: {e}")

# AWS Credentials example (For demonstration purposes)
print(f"AWS Access Key: {aws_access_key}")
print(f"AWS Secret Key: {aws_secret_key}")


print(encrypt("default_access_key"))