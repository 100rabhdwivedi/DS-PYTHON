'''
Class and object 
Accessing attribute and method using object
'''

class Factory:
    a = 12
    def hello(self):
        print("Hello how are you")


obj = Factory()

print(obj.a)
obj.hello()