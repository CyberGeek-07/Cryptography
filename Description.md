This Python-based cryptography tool is designed to securely encrypt and decrypt messages using the AES (Advanced Encryption Standard) algorithm in CBC (Cipher Block Chaining) mode.
The tool generates a shared secret key and an initialization vector (IV) for encryption.
It pads the plaintext to fit the block size, encrypts it, and appends the IV to the ciphertext.
The tool also provides functionality to decrypt the ciphertext, removing the padding to retrieve the original plaintext message. 
The example code demonstrates encrypting a dictionary of messages, converting them into their hexadecimal representations.



P.S. : variable declared here i.e. message_data can contain any message according to your will.
