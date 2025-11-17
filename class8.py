#while loop

a = 1

while a<=10:
    print(a)
    a+=1

#break 

i = 1
n= int(input("Enter a number"))    
while i<12:
    if(i==11):
        i+=1
        continue
    if i==13:
        break
    print(i*n)
    i+=1
else:
    print("Printed the table")

