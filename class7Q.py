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
