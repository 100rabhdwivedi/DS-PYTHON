#1. Count the lower and upper case of the string 
str = input()
ucount = 0
lcount = 0 

for ch in str:
    if ch.isupper():
        ucount+=1
    elif ch.islower():
        lcount+=1
print(f"Uppercase: {ucount}")
print(f"Lowercase: {lcount}")   