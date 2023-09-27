from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC

# Encrypt the file using AES in CFB mode
def encrypt_file(key, filename):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)

    with open(filename, "rb") as file:
        plaintext = file.read()
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    return iv, ciphertext

# Generate MAC for integrity and authenticity
def generate_mac(key, data):
    mac = HMAC(key, hashes.SHA256())
    mac.update(data)
    return mac.finalize()

def sender_main():
    secret_file = "secret.txt"
    
    # Load the secret key from the file
    with open("secret_key.txt", "rb") as key_file:
        shared_secret_key = key_file.read()

    iv, encrypted_data = encrypt_file(shared_secret_key, secret_file)
    mac_key = get_random_bytes(32)
    mac_tag = generate_mac(mac_key, encrypted_data)

    print("Shared Secret Key:", shared_secret_key.hex())
    print("Encryption and MAC generation complete.")

    print("Computed MAC Tag:", mac_tag.hex())

    # Save the encrypted file and MAC tag
    with open("encrypted.txt", "wb") as encrypted_file, open("mac_tag.txt", "wb") as mac_file:
        encrypted_file.write(iv + encrypted_data)
        mac_file.write(mac_tag)

    print("Encrypted file saved as encrypted.txt")
    print("MAC tag saved as mac_tag.txt")

if __name__ == "__main__":
    sender_main()
