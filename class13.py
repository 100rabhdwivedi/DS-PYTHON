s1 = {10,20,30}
s2 = {30,20,40,50}

for elem in s1:
    print(elem)

for elem in enumerate(s1):
    print(elem)  

print(s1.union(s2),s1|s2)   
print(s1.intersection(s2),s1&s2)   
print(s1.difference(s2),s1-s2) #Remove simpilar value to set1 and return a unique value from set1 
print(s2.difference(s1),s2-s1) #Remove simpilar value to set2 and return a unique value from set2

