from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# this is first_1 (key)
print(f"print key: {key}")

# Encrypt a message
message = b"Hello, Hassan!"
encrypted_message = cipher.encrypt(message)
print(f"Encrypted: {encrypted_message}")


# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
print(f"Decrypted: {decrypted_message.decode()}")