from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC

# Decrypt the file using AES in CFB mode
def decrypt_file(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data

# Generate MAC for integrity and authenticity
def generate_mac(key, data):
    mac = HMAC(key, hashes.SHA256())
    mac.update(data)
    return mac.finalize()

# Verify the MAC
def verify_mac(key, data, received_mac_tag):
    computed_mac_tag = generate_mac(key, data)
    return computed_mac_tag == received_mac_tag

def receiver_main():
    encrypted_file = "encrypted.txt"
    mac_file = "mac_tag.txt"
    
    # Load the secret key from the file
    with open("secret_key.txt", "rb") as key_file:
        shared_secret_key = key_file.read()
    
    print("Shared Secret Key:", shared_secret_key.hex())

    with open(encrypted_file, "rb") as file, open(mac_file, "rb") as mac_f:
        received_data = file.read()
        received_mac_tag = mac_f.read()

        iv = received_data[:16]
        ciphertext = received_data[16:]

        decrypted_data = decrypt_file(shared_secret_key, iv, ciphertext)
        decrypted_data = decrypted_data.decode('utf-8')
        print("Decrypted Data:", decrypted_data)
        

        if verify_mac(shared_secret_key, decrypted_data, received_mac_tag):
            print("\nReceiver's Part Completed")
            
            print("MAC tag verification successful. The data is authentic and intact.")
        else:
            print("MAC tag verification failed. The data may have been tampered with.")

if __name__ == "__main__":
    receiver_main()
