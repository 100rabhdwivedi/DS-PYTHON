"""
Dunder method
#__str__

#__len__

#__add__
"""

class Book:
    def __init__(self,title):
        self.title = title

    def __str__(self):
        return self.title 

    def __len__(self):
        return len(self.title)       
    

b1 = Book("Python")

print(b1)
print(len(b1))

class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,custom):
        return self.num + custom.num

a1 =  Number(10)  
a2 = Number(20)

print(a1+a2)
