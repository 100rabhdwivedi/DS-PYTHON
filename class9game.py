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

#2. Stone,Paper ,Scissors

import random 

cscore = 0
uscore = 0

while True:

    cum = random.randint(1,3)
    user = int(input("Press 1 for stone,2 for paper,3 for scissors"))
    print(f"Computer chose: {cum}\n")
    print(f"Computer score {cscore} user score {uscore}\n")

    if cum == 3 and user == 2:
        print("Computer won the round :\n")
        cscore+=1
    elif cum == 1 and user == 3:
        print("Computer won the round :\n")
        cscore+=1
    elif cum == 2 and user == 1:
        print("Computer won the round :\n")
        cscore+=1
    elif cum == user:
        print("Draw the match:")
    else :
        uscore+=1
        print("User won the round :\n")    

    if cscore==5:
        print("Congratulation computer won the game 🤖")    
        break
    if uscore == 5:
        print("Congratulation user won the game 👹")
        break