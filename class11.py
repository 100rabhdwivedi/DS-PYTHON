#list is a hetrogenous nature 
a = [12,13,"saurabh",{"xyz":"prq"},(1,2,3)]

#list is used to store duplicate value

b= [1,22,3,3,22,1,44,22,44]

#list is mutable

b[0]=10
print(b)

#list also support slicing
print(b[:3])

#Refrence copy

list1 = [5,8,9,10]
list2 = list1

list2[1] = 80

print(list1,list2)

#Shallow copy
import copy 
li1 = [2,20,30,40,10]
li2 = li1.copy()

li2[0] = 30
print(li1,li2)

#Deepcopy

import copy 

lis1 = [30,20,50,33]
lis2 = copy.deepcopy(lis1)

lis2[3]=40

print(lis1,lis2)
