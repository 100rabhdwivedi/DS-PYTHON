"""
Inheritance
"""

class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name = {self.name} Age = {self.age}")


class Child(Parent):
    def __init__(self, name, age,background):
        super().__init__(name, age)
        self.background = background

    def show(self):
        super().show()
        print(f"Background = {self.background}")


obj = Parent("xyz",53)
obj2 = Child("xyz",53,"Middle class")

obj.show()
obj2.show()