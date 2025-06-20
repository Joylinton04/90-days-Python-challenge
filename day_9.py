# Day 9 of py challenge
# Create a program that takes user input for a number and catches errors if the user inputs something
# invalid (non-integer). 


try:
    user_input = int(input("Enter an Integer: "))
    print("Your input was", user_input)
except ValueError:
    print("You input is invalid. Kindly enter an Integer")
    

    

    