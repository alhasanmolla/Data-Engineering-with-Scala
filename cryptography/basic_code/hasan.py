import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import os
import sys

# Configuration constants for encryption
# These are the default values for demonstration purposes.
# Replace these with securely generated values in a real-world application.

#DEFAULT_KEY = "youtube_project"  # Example key for encryption
#DEFAULT_IV = "1234567890abcdef"  # Example IV (16 characters = 16 bytes)
#DEFAULT_SALT = "example_salt_value"  # Example salt for key derivation

#######################################################################

DEFAULT_KEY = "youtube_project"  # Example key for encryption
DEFAULT_IV = "youtube_encyptyo"  # Example IV (16 characters = 16 bytes)
DEFAULT_SALT = "youtube_AesEncryption"  # Example salt for key derivation

#######################################################################

# Use environment variables for secure configuration (override defaults if set)
key = os.getenv('ENCRYPTION_KEY', DEFAULT_KEY)
iv = os.getenv('ENCRYPTION_IV', DEFAULT_IV)
salt = os.getenv('ENCRYPTION_SALT', DEFAULT_SALT)

if not (key and iv and salt):
    print("Error: Missing key, IV, or salt configuration.")
    sys.exit(1)

# Constants for AES
BS = 16  # Block size for AES
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')  # Padding function
unpad = lambda s: s[0:-ord(s[-1:])]  # Unpadding function

def get_private_key():
    """
    Derives a secure 32-byte private key using PBKDF2.
    """
    Salt = salt.encode('utf-8')
    kdf = PBKDF2(key, Salt, dkLen=32, count=1000)  # Derive a 32-byte key
    return kdf

def encrypt(raw):
    """
    Encrypts the input plaintext using AES encryption in CBC mode.

    Args:
        raw (str): The plaintext to encrypt.

    Returns:
        str: The base64-encoded encrypted string.
    """
    raw = pad(raw)
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    encrypted = cipher.encrypt(raw)
    return base64.b64encode(encrypted).decode('utf-8')  # Encode as base64 for safe storage/transmission

def decrypt(enc):
    """
    Decrypts the input ciphertext using AES encryption in CBC mode.

    Args:
        enc (str): The base64-encoded encrypted string.

    Returns:
        str: The decrypted plaintext.
    """
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted = cipher.decrypt(base64.b64decode(enc))
    return unpad(decrypted).decode('utf-8')  # Decode to UTF-8 string

# Example usage
if __name__ == "__main__":
    try:
        # Input data for encryption
        plaintext = "Hello, Secure World!"
        print(f"Original Plaintext: {plaintext}")

        # Encrypt
        encrypted_text = encrypt(plaintext)
        print(f"Encrypted Text: {encrypted_text}")

        # Decrypt
        decrypted_text = decrypt(encrypted_text)
        print(f"Decrypted Text: {decrypted_text}")

        # Example: Printing Configuration Values
        print("\nConfiguration Values:")
        print(f"Key: {key}")
        print(f"IV: {iv}")
        print(f"Salt: {salt}")

    except Exception as e:
        print(f"An error occurred: {e}")


print(decrypt("Jocepn+Aon8ika6j3lezoiM0NBv8nPRcUknKq34z7po="))