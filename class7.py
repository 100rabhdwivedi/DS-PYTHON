#Print a table

num = int(input("Entera any number:"))

for i in range (1,11):
    print(f"{num} * {i} = {num*i}")

str = "hello my name is saurabh"

#first way to print string all character
for i in str:
    print(i)

#second way to print string all character
for i in range(0,len(str)):
    print(str[i])    