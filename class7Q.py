# 1. Sum of 1 to n
n1 = int(input("Enter a number till where you want to add- "))
s = 0
for i in range(n1, 0, -1):
    s += i
print(f"Sum of 1 to {n1} = {s}") 


# 2. Factorial
n2 = int(input("Enter a number whose factorial you want: "))
fact = 1
for i in range(1, n2 + 1):
    fact *= i
print("Factorial =", fact)


# 3. Even & Odd sum
n3 = int(input("Enter the number till where you want to get even or odd sum- "))

esum = 0
odsum = 0

for i in range(1, n3 + 1):
    if i % 2 == 0:
        esum += i
    else:
        odsum += i

print("Even sum =", esum)
print("Odd sum =", odsum)

# 4.Find the factors of number

num = int(input("Enter a number that's factor you want:"))

for i in range (1,num+1):
    if num%i ==0:
        print(i)

#5 sum of all factors
num1 = int(input("Enter a number that's factor you want:"))
sm=0
for i in range (1,num1+1):
    if num1%i ==0:
        sm+=i
print(f"Sum of factors: {sm}") 


#6 power calculation

a = int(input("Enter a number ")) 
b = int(input("Enter a power"))  

ans=1
for i in range(1,b+1):
    ans*=a

print("Answer = ",ans)

# 7.Prime number checker

number1 = int(input("Enter a number "))

for i in range (2,number1//2+1):
    if number1%i == 0:
        print("Composite number")    
        break

else:
    print("Prime number")
