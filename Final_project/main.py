#Library management system
import random
import string
import json
from datetime import datetime
from pathlib import Path

class Library:

    file_name = "library.json"
    data = {"books":[],"members":[]}
    
    if Path(file_name).exists():
        with open(file_name,'r') as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)


    @classmethod
    def save_data(cls):
        with open(cls.file_name,'w') as f:
            json.dump(cls.data,f,indent=4,default="str")


    def gen_id(prefix = "B"):
        id = ""
        for i in range(5):
            id+= random.choice(string.ascii_uppercase + string.digits)
        return prefix+id
    

    def create_book(self):
        name = input("Enter book name :")
        author = input("Enter author name :")
        stock = int(input("Enter stock quntity :"))

        book = {
            "id":Library.gen_id(),
            "name":name,
            "author":author,
            "stock":stock,
            "available_stock":stock,
            "created_at":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        Library.data['books'].append(book)
        Library.save_data()



print("="*50)
print("Welcome to library management system")
print("="*50)
print("1. Add a book")
print("2. List of a book")
print("3. Delete a book")
print("4. Search a book")
print("5. Add a member")
print("6. Display a member")
print("7. Borrow a book")
print("8. Return a book")
print("Press e to exit")

choice = int(input("Enter your choice here :"))

l1 = Library()

if choice == 1:
    l1.create_book()
