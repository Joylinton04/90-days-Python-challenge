# Day 19-20 of py challenge
# Create a simple encryption/decryption tool using the cryptography library (e.g., AES encryption).


from cryptography.fernet import Fernet

# Step 1: Generate a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Step 2: Load the key from the file
def load_key():
    return open("secret.key", "rb").read()

# Step 3: Encrypt a message
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# Step 4: Decrypt a message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()
    return decrypted

# ============ MAIN PROGRAM =============
if __name__ == "__main__":
    # Only run once to generate key
    # generate_key()

    key = load_key().decode('utf-8')

    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

    if choice == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted = encrypt_message(message, key)
        print(f"🔐 Encrypted: {encrypted.decode()}")

    elif choice == 'd':
        encrypted_input = input("Enter the encrypted message: ")
        try:
            decrypted = decrypt_message(encrypted_input.encode(), key)
            print(f"🔓 Decrypted: {decrypted}")
        except Exception as e:
            print("❌ Decryption failed:", e)

    else:
        print("Invalid choice. Choose 'e' or 'd'.")
