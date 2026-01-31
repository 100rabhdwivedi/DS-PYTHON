from pathlib import Path
import os


def create_folder():
    folder_name = input("Enter folder name :") 
    try:
        p = Path(folder_name)
        p.mkdir()
        print("Folder created successfully:")
    except Exception as err:
        print(f"Error: {err}")

def show_folder():
    try:
        p = Path("")
        items = list(p.rglob("*"))
        for item in items:
            print(f"{item.name}")

    except Exception as err:
            print(f"Error: {err}")   

def delete_folder():
    try:
        show_folder()
        folder_name = input("Enter a folder name that you want to delete :")
        p = Path(folder_name)
        p.rmdir()
        print("You folder has been deleted :")
    except Exception as err:
        print(f"Error: {err}")       

def update_folder():
    try:
        show_folder()
        old_name = input("Enter old folder name that you want to update:")
        new_name = input("Enter new folder name that you want to set:")
        p = Path(old_name)
        p.rename(new_name)
    except Exception as err:
        print(f"Error: {err}")    


print("Press 1 to create folder :")
print("Press 2 to read folder :")
print("Press 3 to update folder :")
print("Press 4 to delete folder :")

choice = int(input("Enter your choice :"))




if choice == 1:
    create_folder()
elif choice == 2:
    show_folder()
elif choice == 3:
    delete_folder()    
elif choice == 4:
    update_folder()
else:
    print("Invalid choice :")            

