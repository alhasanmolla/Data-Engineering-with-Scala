from cryptography.fernet import Fernet

# Replace this with your actual encryption key in > (first.py)
key = b'1GP98yGHOmISL3OZ7bib_ULB5JUNm0r4M0i_2eoqVIk='  # This needs to be the correct key used during encryption
cipher = Fernet(key)

# Provide your encrypted message
encrypted_message = b"gAAAAABneVe9TBLS1jeh7bo_Ag1gXI4Gu6zQndhziqxMg4-vw-7WGtRwe28rj0jQRA-l1_3UFtg4_NKDPvtJ7MZ0tQBfPXXOJA=="

# Decrypt the message
try:
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message.decode()}")
except Exception as e:
    print(f"An error occurred during decryption: {e}")