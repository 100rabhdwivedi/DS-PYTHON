"""
Learning constructor
"""

class Factory:

    def __init__(self,material,capacity,price):
        self.material = material
        self.capacity = capacity
        self.price = price

    def show(self):
        print(self.material,self.capacity,self.price)    

obj = Factory("Leather",'30kg',2000)  
obj.show()