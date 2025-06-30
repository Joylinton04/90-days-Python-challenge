# Day 18 of py challenge
# Cryptography is the practice and study of techniques for secure communication
# Write a Python script that hashes a user’s password and compares it to a known hash.

import hashlib

known_hash = hashlib.sha256('linton1234'.encode('utf-8')).hexdigest()

user_password = input("Enter your password: ")
password_bytes = user_password.encode('utf-8')

hasher = hashlib.sha256()
hasher.update(password_bytes)
hex_digest = hasher.hexdigest()

if hex_digest == known_hash:
    print("✅ Password match!")
else:
    print("❌ Password does not match.")
    
