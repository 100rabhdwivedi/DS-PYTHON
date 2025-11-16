#1. sum of 1 to n

n= int(input("Enter a number till where you want to add-"))

s=0

for i in range(n,0,-1):
    s+=i
print(f"Sum of 1 to n= {s}") 

# 2.Factorial of a number

n = int(input("Enter a number that's factorial you want:"))
fact = 1

for i in range(1,n):
    fact*=i
print("Factorial = ",fact)    

#3. sum of even and odd seperately

n = int(input("Enter the number till where you want to get even or odd sum-"))

esum=0
odsum=0

for i in range(1,n):
    if i%2==0:
        esum+=i
    else:
        odsum+=i    
print(f"Even sum = {esum}")   
print(f"Odd sum = {odsum}")     