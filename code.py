import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
shared_secret_key = os.urandom(32)
def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_message = message + (16 - len(message) % 16) * chr(16 - len(message) % 16)
    ciphertext = encryptor.update(padded_message.encode()) + encryptor.finalize()
    return iv + ciphertext
def decrypt_message(ciphertext, key):
    iv = ciphertext[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    return plaintext.decode()
message_data = {
    "person1": [
        {"message": "I love eating pizza?"},
        {"message": "Would you eat with me?"}
    ],
    "person2": [
        {"message": "Usually I Eat Healthy"},
        {"message": "Never Mind one day wont hurt"}
    ]
}

for person, messages in message_data.items():
    for message in messages:
        encrypted_message = encrypt_message(message["message"], shared_secret_key)
        message["message"] = encrypted_message.hex()

print("Encrypted message_data dictionary:")
print(message_data)
