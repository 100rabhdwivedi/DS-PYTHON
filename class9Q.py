#Print greeting
def welcome_message(name):
    return f"Welcome, {name}!"


print(welcome_message("saurabh"))

#Check the number is positive,negative,zero

def check_number_sign(num):
    # Write your code here
    if num>0:
        return "Positive"
    elif num <0 :
        return "Negative"
    else :
        return "Zero"
print(check_number_sign(20))  

#Check even and odd 

def check_even(num):
    # Write your code here
    if num %2 == 0:
        return "Even"
    else :
        return "Odd"
    pass

print(check_even(30))

#Multiplication table 

def print_table(n):
    # Write your code here
    for i in range (1,11):
        print(f"{n} x {i} = {n*i}")
num = int(input("Enter a number for table :"))        
print_table(num)        