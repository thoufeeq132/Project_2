import admin
import user

class Main:
    admin = admin.Admin()
    user = user.User()

    def __init__(self,choice):
        self.choice= choice

    def execute_admin(self):
        if self.choice==1:
            Main.admin.display_book
        elif self.choice==2:
            Main.admin.add_book()
        elif self.choice==3:
            Main.admin.remove_book()
        elif choice==4:
            exit()

    def execute_user(self):
        if self.choice==1:
            Main.user.display()
        elif self.choice==2:
            Main.user.Borrow_Book()
        elif self.choice==3:
            Main.user.Return_Book()
        elif choice==4:
            exit()


if __name__=="__main__":
    print("Welcome to The Library")
    choice = int(input("Press 1 to Login as Admin/n Press 2 to Login as User"))
    if choice==1:
        print("Enter 1. To Display the list of Available Books")
        print("Enter 2. To Add a Book")
        print("Enter 3. To Remove a Book")
        print("Enter 4. To Edit a Book")
        print("Enter 5. To Exit")
        choice = int(input())
        obj = Main(choice)
        obj.execute_admin()
        
    elif choice==2:
        print("Enter 1. To Display the list of Available Books")
        print("Enter 2. To Borrow a Book")
        print("Enter 3. To Return a Book")
        print("Enter 4. To Exit")
        choice = int(input())
        obj = Main(choice)
        obj.execute_user()

    else:
        print("Invalid option")