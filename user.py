import admin
import json
admin = admin.Admin()

class User:
    def __init__(self):
        pass

    def display(self):
        admin.display_book()

    def Borrow_Book(self):
        admin.display_book()
        X=input("Which book you want to borrow:")
        with open("book.json","r") as file:
            self.books=json.load(file)
        print("Book you've borowwed:")
        for k,v in self.books.items():
            if k==X:
                print(v["Book_Name"])
                v["Quantity"]-=1

        with open("book.json","w") as file:
            json.dump(self.books,file)

    def Return_Book(self):
        X=input("Please enter the Book ID of the Book you want to Return:")
        with open("book.json","r") as file:
            self.books=json.load(file)
        for k,v in self.books.items():
            if k==X:
                print(v["Book_Name"])
                v["Quantity"]+=1

        with open("book.json","w") as file:
            json.dump(self.books,file)

        print("Book Returned Successfully!!!")