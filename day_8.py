# Day 8 of py challenge
# Write a script that reads a text file and counts how many lines and words are in the file.

with open('test.txt', 'r') as file:
    lines = 0
    for line in file:
        lines += 1
        print(line)
        
print("Total lines: ", lines)
