#1. average of the list

list1 = [20,30,40,60,90]

sum=0
for i in range(len(list1)):
    sum+=list1[i]

print("Average =",sum//(len(list1)))    

#2. find the greatest number 

list2 = [20,30,44,55,22,80,90,890,678,556,34456,9087,456,234567,987654,23434,9876,4567,87345,89787]

max = 0

for i in range (len(list2)):
    if max < list2[i]:
        max = list2[i]

print("Max value =",max)