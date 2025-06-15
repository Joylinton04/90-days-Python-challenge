# Day 5 of py challenge
# Write a function that takes a number as input and returns the factorial of that number.


def fac(n):
    if n < 0 or int(n) != n:
        return "Invalid input. Use a non-negative integer."
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)

    
         
print(fac(5))
    