from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

# Load or generate RSA key pair for sender
sender_private_key = None
sender_public_key = None

# Check if the keys are already generated
if os.path.exists("sender_private_key.pem") and os.path.exists("sender_public_key.pem"):
    with open("sender_private_key.pem", "rb") as private_key_file, open("sender_public_key.pem", "rb") as public_key_file:
        sender_private_key = RSA.import_key(private_key_file.read())
        sender_public_key = RSA.import_key(public_key_file.read())
else:
    # Generate RSA key pair for sender
    sender_private_key = RSA.generate(2048)
    sender_public_key = sender_private_key.publickey()

    # Save the keys to files
    with open("sender_private_key.pem", "wb") as private_key_file, open("sender_public_key.pem", "wb") as public_key_file:
        private_key_pem = sender_private_key.export_key()
        private_key_file.write(private_key_pem)

        public_key_pem = sender_public_key.export_key()
        public_key_file.write(public_key_pem)

# Encrypt the data using AES in CFB mode
def encrypt_data(key, data):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    ciphertext = cipher.encrypt(data)
    return iv, ciphertext

# Calculate the hash using SHA-256
def calculate_hash(data):
    hasher = SHA256.new(data)
    return hasher.digest()

# Sign the hash using sender's private key
def sign_hash(private_key, data_hash):
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(SHA256.new(data_hash))
    return signature

# Decrypt the data using AES in CFB mode
def decrypt_data(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data

# Verify the signature using sender's public key
def verify_signature(public_key, data_hash, signature):
    verifier = pkcs1_15.new(public_key)
    try:
        verifier.verify(SHA256.new(data_hash), signature)
        return True
    except Exception:
        return False

# Sender's Part
def sender_main():
    secret_data = input("Enter the secret data: ")

    aes_key = get_random_bytes(32)
    iv, encrypted_data = encrypt_data(aes_key, secret_data.encode("utf-8"))

    encrypted_hash = calculate_hash(encrypted_data)
    signature = sign_hash(sender_private_key, encrypted_hash)

    return aes_key, iv, encrypted_data, encrypted_hash, signature

# Receiver's Part
def receiver_main(aes_key, iv, encrypted_data, encrypted_hash, signature):
    signature_verified = verify_signature(sender_public_key, encrypted_hash, signature)

    if signature_verified:
        decrypted_data = decrypt_data(aes_key, iv, encrypted_data)
        print("\nReceiver's Part Completed")
        print("Decrypted Data:", decrypted_data.decode("utf-8"))
    else:
        print("Signature verification failed. The data may not be authentic.")

if __name__ == "__main__":
    aes_key, iv, encrypted_data, encrypted_hash, signature = sender_main()
    print("Sender's Part Completed")
    print("Encrypted Data:", encrypted_data)

    # Simulate sending and receiving
    received_aes_key = aes_key
    received_iv = iv
    received_encrypted_data = encrypted_data
    received_encrypted_hash = encrypted_hash
    received_signature = signature

    receiver_main(received_aes_key, received_iv, received_encrypted_data, received_encrypted_hash, received_signature)
