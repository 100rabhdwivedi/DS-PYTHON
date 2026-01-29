'''
Lambda function ,
map , filter , zip,
list, set, dictionary comprehension
'''

#Creating a lambda function 

# square = lambda a : a**2

# print("Square =", square(10))

#Using a map function 

# lis = [1,2,3,4]

# out = map(lambda lis : lis ** 2,lis)

# print(list(out))

# Finding a even numbers using filter function

# lis = [1,2,3,4,5,6,7]

# even = filter(lambda lis : lis % 2 == 0,lis)

# print(list(even))

#Use of zip function 

# name = ['gaurav','sumit','anurag','xyz']

# age = [22,34,50,12]

# comb = list(zip(name,age))

# print(comb)

#List comprehension

# chairsCount = [1,2,3,4,5,6,10,18,30,22,6,3,4]

# count = [i for i in chairsCount if i> 10] 
# print("Count = ",count)

#Set comprehension

# chairsCount = [1,2,3,5,6,10,20,20,40,38,39,38,50]

# count = {i for i in chairsCount if i > 10}
# print("Count =",count)

#dic comprehension

# chairsCount = [1,2,3,5,6,10,20,20,40,38,39,38,50]

# squareCount = {i:i**2 for i in chairsCount if i > 10}
# print("Count =",squareCount)



