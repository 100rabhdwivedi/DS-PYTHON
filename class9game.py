#Guess the number

import random 

num = random.randint(1,100)
tries = 0
while True:
    gusnum = int(input("Enter the number between 1 to 100: "))
    tries+=1
    if num == gusnum:
        print(f"Congratulation you have gussed a right number in {tries} tries")
        break
    elif gusnum < num :
        print("You need to guess upper value:")    
    elif gusnum > num :
        print("You need to guess lower value:")    
    else :
        print("Enter a valid number")    
