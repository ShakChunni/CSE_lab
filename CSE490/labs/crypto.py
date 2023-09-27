from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


def aes_encrypt(plaintext, key, mode):
    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == "CBC":
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
    else:
        raise ValueError("Invalid AES mode. Please choose either ECB or CBC.")

    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()


def aes_decrypt(ciphertext, key, mode):
    ciphertext = base64.b64decode(ciphertext)
    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode == "CBC":
        iv = ciphertext[: AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = ciphertext[AES.block_size :]
    else:
        raise ValueError("Invalid AES mode. Please choose either ECB or CBC.")

    try:
        decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return decrypted_text.decode()
    except ValueError as e:
        print("Error during decryption:", e)
        return None


# RSA


def rsa_encrypt(plaintext, public_key):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(plaintext)
    return ciphertext


def rsa_decrypt(ciphertext, private_key):
    cipher_rsa = PKCS1_OAEP.new(private_key)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext


# HASHING
def generate_hash(data, hash_mode):
    if hash_mode == "SHA1":
        hash_object = hashlib.sha1()
    elif hash_mode == "SHA256":
        hash_object = hashlib.sha256()
    elif hash_mode == "SHA512":
        hash_object = hashlib.sha512()
    else:
        raise ValueError(
            "Invalid hash mode. Please choose either SHA1, SHA256, or SHA512."
        )

    hash_object.update(data.encode())
    hash_value = hash_object.hexdigest()
    return hash_value


# DIGITAL SIGN
def generate_signature(message, private_key):
    key = RSA.import_key(private_key)
    h = SHA256.new(message.encode())
    signer = pkcs1_15.new(key)
    signature = signer.sign(h)
    return signature


def verify_signature(message, signature, public_key):
    key = RSA.import_key(public_key)
    h = SHA256.new(message.encode())
    verifier = pkcs1_15.new(key)
    try:
        verifier.verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False


# MAC
def generate_mac(data, algorithm):
    if algorithm == "MD5":
        hash_object = hashlib.md5()
    elif algorithm == "SHA1":
        hash_object = hashlib.sha1()
    elif algorithm == "SHA256":
        hash_object = hashlib.sha256()
    else:
        raise ValueError(
            "Invalid MAC algorithm. Please choose either MD5, SHA1, or SHA256."
        )

    hash_object.update(data.encode())
    mac_value = hash_object.hexdigest()
    return mac_value


# Getting inputssss
mode = input("Enter the mode (AES, RSA, HASH, SIGN or MAC): ")

if mode.lower() == "aes":
    operation = input("Enter the operation (Encrypt or Decrypt): ")
    plaintext_or_ciphertext = input("Enter the plaintext or ciphertext: ")
    key = input("Enter the AES key (16 bytes): ")
    aes_mode = input("Enter the AES mode (ECB or CBC): ")

    if operation.lower() == "encrypt":
        if plaintext_or_ciphertext:
            ciphertext = aes_encrypt(plaintext_or_ciphertext, key.encode(), aes_mode)
            print("Ciphertext:", ciphertext)
        else:
            print("Please provide the plaintext.")
    elif operation.lower() == "decrypt":
        if plaintext_or_ciphertext:
            plaintext = aes_decrypt(plaintext_or_ciphertext, key.encode(), aes_mode)
            print("Decrypted Text:", plaintext)
        else:
            print("Please provide the ciphertext.")
    else:
        print("Invalid operation. Please choose either Encrypt or Decrypt.")

elif mode.lower() == "rsa":
    operation = input("Enter the operation (Encrypt or Decrypt): ")
    plaintext_or_ciphertext = input("Enter the plaintext or ciphertext: ")
    key = input("Enter the RSA key (PEM format): ")

mode = input("Enter the mode (AES, RSA, HASH, SIGN, or MAC): ")

if mode.lower() == "aes":
    operation = input("Enter the operation (Encrypt or Decrypt): ")
    plaintext_or_ciphertext = input("Enter the plaintext or ciphertext: ").strip()
    key = input("Enter the AES key (16 bytes): ")
    aes_mode = input("Enter the AES mode (ECB or CBC): ")

    if operation.lower() == "encrypt":
        if plaintext_or_ciphertext:
            ciphertext = aes_encrypt(plaintext_or_ciphertext, key.encode(), aes_mode)
            print("Ciphertext:", ciphertext)
        else:
            print("Please provide the plaintext.")
    elif operation.lower() == "decrypt":
        # Fixed ciphertext for demonstration purposes
        ciphertext = b"YGIlvpJrtDgmhCqWfIUd7Q=="
        if ciphertext:
            plaintext = aes_decrypt(ciphertext, key.encode(), aes_mode)
            if plaintext is not None:
                print("Decrypted Text:", plaintext)
        else:
            print("Please provide the ciphertext.")
    else:
        print("Invalid operation. Please choose either Encrypt or Decrypt.")

elif mode.lower() == "hash":
    plaintext = input("Enter the plaintext: ")
    hash_mode = input("Enter the hash mode (SHA1, SHA256, or SHA512): ")
    # Generate the hash value
    hash_value = generate_hash(plaintext, hash_mode)
    print("Hash value:", hash_value)

elif mode.lower() == "sign":
    operation = input("Enter the operation (Generation or Verification): ")
    message = input("Enter the message: ")
    if operation.lower() == "generation":
        private_key = input("Enter the private key (PEM format): ")
        signature = generate_signature(message, private_key)
        print("Digital Signature:", signature.hex())
    elif operation.lower() == "verification":
        signature = input("Enter the digital signature (in hexadecimal format): ")
        public_key = input("Enter the public key (PEM format): ")
        is_valid = verify_signature(message, bytes.fromhex(signature), public_key)
        if is_valid:
            print("Digital Signature is valid.")
        else:
            print("Digital Signature is not valid.")

elif mode.lower() == "mac":
    message = input("Enter the message: ")
    mac_algorithm = input("Enter the MAC algorithm (MD5, SHA1, or SHA256): ")

    # Generate the MAC value
    mac_value = generate_mac(message, mac_algorithm)
    print("MAC value:", mac_value)

else:
    print("Invalid mode.")
