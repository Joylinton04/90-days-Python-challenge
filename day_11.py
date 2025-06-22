# Day 11 of py challenge
# Build a program that validates email addresses using regular expressions.

import re


def verify_email():
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.(com|net)"
    user_email = str(input("Enter your email: "))
    if(re.match(email_pattern, user_email)):
        print("Your email is valid")
    else:
        print("Invalid email")
        

verify_email()