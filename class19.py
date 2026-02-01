class Greet:
    message = "hello how are you"

    def printGreet(self):
        print(f"{self.message}")

    print("Simplely come to the class:")    

print(Greet.message)    
Greet.printGreet(Greet)