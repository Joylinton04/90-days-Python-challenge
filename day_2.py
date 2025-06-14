# Day 2 of py challenge
# Create a program that takes user input for their name and age, then prints a greeting with their name
# and calculates the year they were born.


name = input("Enter your name: ")
age = int(input("Enter your age: "))

year_born = 2025 - age
print("Hello", name)
print("You were born in", year_born)

