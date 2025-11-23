#tuple has a hetrogenous nature

tp = (1,2,"str1",3.0)

#tuple also aloow to store duplicate value

tp1=(1,1,2,2,3,3)

#tuple is immutable

# tp1[0] = 12 #not allowed

#tuple unpacking

a,b,c=(10,20,30)

print(c)

#traversing on tuple
#method1
for i in tp:
    print(i)
#method2   
for j in range(len(tp)):
    print(tp[j]) 

#tuple methods
print('\n')
print(tp1.count(3))
print(tp1.index(3))
