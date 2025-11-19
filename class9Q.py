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
