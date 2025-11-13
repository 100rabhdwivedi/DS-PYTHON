#1. Compare two numbers

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

if num1==num2:
    print("Both are equal:")
elif num1>num2:
    print(f"First number is greater: {num1}")
else :
    print(f"Second number is greater: {num2}")        

#2. Greet by gender(m/f)

gender = input("Enter your gender m/f")

if gender == 'm':
    print("Hello sir")
elif gender == 'f':
    print("Hello ma'am")
else:
    print("Enter a valid input")  

#3.Leap year 

year = int(input("Enter a year:"))

if year % 100 == 0 and year % 400 == 0:
    print("Leap year:")
elif year % 100 != 0 and year % 4 == 0:
    print("Leap year:")
else:
    print("Simple year") 

#4. vowel and consonent 

ch = input("Enter any alphabet :-")

if ch in "aeiouAEIOU":
    print("Vowel")
else :
    print("Consonent")    
