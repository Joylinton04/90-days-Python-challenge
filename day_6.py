# Day 6 of py challenge
# Create a program that takes a list of numbers and prints the sum and average.


def cal(arr):
    sum = 0
    for num in arr:
        sum += num
        
    average = len(arr)/sum   
    print(f"Total: {sum}")
    print(f"Average: {average:.2f}")
    
    
    
arr = [1,2,3,4,5]
cal(arr)