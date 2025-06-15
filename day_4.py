# Day 4 of py challenge
# Create a simple "countdown" program that counts down from 10 to 1 using a while loop.

from time import sleep


start = 10
print("\nCountdown program")

while start > -1:
    print(start)
    start -= 1
    sleep(1)
    
