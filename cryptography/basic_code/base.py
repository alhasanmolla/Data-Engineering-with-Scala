import os
import base64

def generate_key():
    # 32-byte key (256 bits)
    return base64.urlsafe_b64encode(os.urandom(32))

def generate_iv():
    # 16-byte IV
    return base64.urlsafe_b64encode(os.urandom(16))

def generate_salt():
    # 16-byte salt
    return base64.urlsafe_b64encode(os.urandom(16))

# জেনারেট করা উপাদান
key = generate_key()
iv = generate_iv()
salt = generate_salt()

print(f"Generated Key: {key.decode()}")
print(f"Generated IV: {iv.decode()}")
print(f"Generated Salt: {salt.decode()}")