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
        try:
            with open(cls.file_name,'w') as f:
                json.dump(cls.data,f,indent=4,default="str")
                print("Data saved successfully :")
        except Exception as err:
            print("Error :",err)    


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

    def list_books(self):
        if not Library.data["books"]:
            print("No books found")
            return
        # Table Header
        print("-" * 85)
        print(f"{'Index':<6} | {'ID':<6} | {'Name':<20} | {'Author':<15} | {'Stock':<6} | {'Available':<9}")
        print("-" * 85)
        # Table Rows
        for idx, item in enumerate(Library.data["books"]):
            print(f"{idx+1:<6} | {item['id']:<6} | {item['name']:<20} | {item['author']:<15} | {item['stock']:<6} | {item['available_stock']:<9}")

        print("-" * 85)

    def add_member(self):
        name = input("Enter member name :")
        email = input("Enter email :")
        member = {
            "id":Library.gen_id("M"),
            "name":name,
            "email":email,
            "borrowed_books":[],
            "created_at":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        Library.data['members'].append(member)
        Library.save_data()

    def list_members(self):
        if not Library.data["members"]:
            print("No members found")
            return
        print("-"*85)
        print(f"{'Index':6} | {'ID':<6} | {'Name':<20} | {'Borrowed books':<6} ")
        print("-"*85)

        for idx , item in enumerate(Library.data['members']):
            print(f"{idx+1:<6} | {item['id']:<6} | {item['name']:<20} | {item['borrowed_books']} |{item['created_at']} ")

        print("-" * 85)

    def borrow_book(self):
        member_id = input("Enter member id:")
        members_data = Library.data['members']

        member = next(filter(lambda m : m["id"] == member_id,members_data),None)

        if not member :
            print("No such member found:")
            return

        
        book_id = input("Enter book id:")
        books_data = Library.data['books']

        book = next(filter(lambda b : b['id'] == book_id,books_data),None)
        if not book :
            print("No such book found:")
            return

        elif(book['available_stock']<=0):
            print("No books are available to be borrowed :")
            return 
        else :

            book_data = {
                "id":book_id,
                "name":book['name'],
                "borrowed_date":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }


            book['available_stock'] -=1
            member['borrowed_books'].append(book_data)
            Library.save_data() 

    def return_book(self):
        member_id = input("Enter member id:")
        members_data = Library.data['members']

        member = next(filter(lambda m : m["id"] == member_id,members_data),None)

        if not member :
            print("No such member found:")
            return

        
        book_id = input("Enter book id:")
        books_data = Library.data['books']

        book = next(filter(lambda b : b['id'] == book_id,books_data),None)
        if not book :
            print("No such book found:")
            return
        
        elif not member['borrowed_books']:
            print("No book has been  borrowed :")
            return
        
        book['available_stock'] +=1

        books_after_return = list(filter(lambda b : b["id"] != book_id,member['borrowed_books']))

        member['borrowed_books'] = books_after_return
        Library.save_data()
        

print("="*50)
print("Welcome to library management system")
print("="*50)
print("1. Add a book")
print("2. List of a book")
print("3. Add a member")
print("4. Display a member")
print("5. Borrow a book")
print("6. Return a book")
print("Press e to exit")

choice = int(input("Enter your choice here :"))

l1 = Library()


if choice == 1:
    l1.create_book()

elif choice == 2:
    l1.list_books()   

elif choice == 3:
    l1.add_member()    

elif choice == 4:
    l1.list_members()

elif choice == 5:
    l1.borrow_book()        

elif choice == 6:
    l1.return_book()