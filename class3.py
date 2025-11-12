name= "saurabh dwivedi"

#Accessing the string

print(name)
print(name[0:2:1])
print(name[-1:0:-1])

#String slicing

str = 'hello i am data scientist'

print(str[0:5])
print(str[11:15])
print(str[16::])

#Formatted string

age = 20

print(f'My name is {name}\nand age is {age}')

#Row string

print(r"This is a row string \n \t \b give permission to print space sequence")

#Type conversion
# int(),float(),bool(),str() these are the methods that's used to convert the type

a= '23'
b=bool(0)
print(int(a))
print(type(a)) #that's used to check the data type of variable
print(b)

#Falsy and truthy
# 0,0.0,"",False,[],{},() these all are falsy value and and excluding these valuse all are thruthy value


#input from user
name1 = input("Enter your name:")

#input from user and convert the string input into integer

age1 = int(input("Enter your age:"))

print(f"My name is {name1} and age is {age}")