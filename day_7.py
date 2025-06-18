# Day 7 of py challenge
# Create a program that stores user information (name, age) in a dictionary and allows the user to
# retrieve it by providing the name.

def ret():
    user_details = {
        "name": str(input("Enter your name: ")),
        "age": input("what is your age: "),
        "height": input("What is your height? ")
    }
    
    print("Get info (Name, age, height)")
    user_input = str(input("> ")).lower()
    print(f"{(user_input).capitalize()}: {user_details[user_input]}")
    
    
ret()

