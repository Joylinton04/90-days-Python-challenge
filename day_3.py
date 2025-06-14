# Day 3 of py challenge
# Build a simple age checker: Ask the user for their age and tell them if they are eligible for certain
# services (e.g., "You are eligible to vote" or "You are too young to vote").

age = int(input("\nWhat is you age? "))

if age > 18:
    print("You are eligible to vote!")
else:
    print("You are too young to vote")