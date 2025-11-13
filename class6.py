#1. if else 
age = int(input("Enter your age:"))

if age>=18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")   


# 2.if else with pass
money = float(input("Enter a amount : "))

if money >=2000:
    pass
else:
    print("Money is lessthan 2000")

#3 turnary operator in py

print("Voter ") if age>=18 else print("Not voter")    