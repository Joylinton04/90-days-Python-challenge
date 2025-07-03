if __name__ == "__main__":
#     # Only run once to generate key
#     # generate_key()

#     key = load_key()

#     choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

#     if choice == 'e':
#         message = input("Enter the message to encrypt: ")
#         encrypted = encrypt_message(message, key)
#         print(f"🔐 Encrypted: {encrypted.decode()}")

#     elif choice == 'd':
#         encrypted_input = input("Enter the encrypted message: ")
#         try:
#             decrypted = decrypt_message(encrypted_input.encode(), key)
#             print(f"🔓 Decrypted: {decrypted}")
#         except Exception as e:
#             print("❌ Decryption failed:", e)

#     else:
#         print("Invalid choice. Choose 'e' or 'd'.")
