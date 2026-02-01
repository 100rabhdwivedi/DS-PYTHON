"""
1. Instance method,
2. Class method,
3. Static method,
4. Constructor
"""

class Decor:
    type = "plastic"

    def __init__(self ,model,size,cost):
        self.model = model
        self.size = size
        self.cost = cost

    #Instance method
    def show_detail(self):
        print(f"Model = {self.model}, Size = {self.size}, Cost = {self.cost}")

    @classmethod
    def show_type(cls):
        print(f"Type = {cls.type}")  

    @staticmethod
    def simple_mes():
        print("Simpelly created")      

m1 = Decor("box",20,2000)

m1.show_detail()
m1.show_type()
m1.simple_mes()



Decor.show_type()
Decor.simple_mes()

