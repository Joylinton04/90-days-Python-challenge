# Day 12 of py challenge
# Create a script that reads a JSON file and prints out specific values based on user input.

import json


def read_json():
    try:
        user_input = str(input("Get (Name | Age | Height | Gender): ")).lower()
        with open("data.json") as file:
            data = json.load(file)

        print(f"Your {(user_input)} is {data["user"][user_input]}")
    except KeyError:
        print("Value should be (Name | Age | Height | Gender")
        read_json()


read_json()