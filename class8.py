#while loop

a = 1

while a<=10:
    print(a)
    a+=1

#break 

i = 1
n= int(input("Enter a number"))    
while i<12:
    if(i==11):
        i+=1
        continue
    if i==13:
        break
    print(i*n)
    i+=1
else:
    print("Printed the table")

#1. Print the first digit of a number like 145 -> 1

n= int(input("Enter a number :"))
num = n
ans =0

while n>0:
    ans = n%10
    n = n//10
print(f"First digit of {num} is {ans}")

#2. Print a reverse of a number like 451 -> 154

n1 = int(input("Enter a number :"))
rev = 0

while n1>0:
    rev = rev *10 + n1%10
    n1//=10

print("Reverse =",rev)

# 3.Automorphic number

num = int(input("Enter a number to check automorphic: "))

copy = num
square = num ** 2
count = 0

while num > 0:
    count += 1
    num //= 10

dig = 0
while count != 0:
    dig = dig * 10 + square % 10
    square //= 10
    count -= 1

rev = 0
while dig > 0:
    rev = rev * 10 + dig % 10
    dig //= 10

if rev == copy:
    print("Automorphic")
else:
    print("Simple")
    