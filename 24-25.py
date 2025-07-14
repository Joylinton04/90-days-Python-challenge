# Day 24-25: Brute Force Password Cracking
# Write a script that attempts to brute-force a password using a wordlist and hashes it with hashlib.

import hashlib

user_password = ''


with open('wordlist.txt', "r") as text:
    line = 0
    for word in text:
        line += 1
        if word.strip() == user_password:
            print(f"Password Found: {user_password}")
            hasher = hashlib.sha256()
            hasher.update(word.strip().encode('utf-8'))
            hex_digest = hasher.hexdigest()
            print(f"Hash: {hex_digest}")
            print(f"Tries: {line}")
            break
    else:
        print(f"Tries: {line}")
        print("Not found")
            
            
        
        
        