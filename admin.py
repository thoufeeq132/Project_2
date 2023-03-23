import json
class Admin:
    def __init__(self):
        self.books = {}
        self.book_data = {}  

    def add_book(self):
        n = int(input("Enter the Number of Books to Add in Library:"))
        with open("book.json","r") as file:
            self.books = json.load(file)
        index = list(self.books.keys())
        print(index)
        print(type(index))
        last_index = int(index[-1])
        for i in range(last_index+1,last_index+n+1):
            self.book_data = {}
            self.book_data['Book_Name'] = input("Book Name")
            self.book_data['Author'] = input("Author")
            self.book_data['Price'] = float(input("Price"))
            self.book_data['Quantity'] = int(input("Quantity:"))
            self.books[i]=self.book_data

        with open("book.json","w") as file:
            json.dump(self.books,file)
        print("Book Added Successfully!!!")

    def remove_book(self):
        with open("book.json","r") as file:
            self.books = json.load(file)
            for k,v in self.books.items():
                print(k,"---->",v)
            print("Enter the Book ID to remove a Book : ")
            remove = input()
            del self.books[remove]
        with open("book.json","w") as file:
            json.dump(self.books,file)
        print("Book Removed Successfully!!!")

                 
    def edit_book(self):
        with open("book.json","r") as file:
            self.books = json.load(file)
            for k,v in self.books.items():
                print(k,"---->",v)
            print("Enter the Book ID For editing : ")
            edit = int(input())
            self.book_data = {}
            self.book_data['Book_Name'] = input("Book Name")
            self.book_data['Author'] = input("Author")
            self.book_data['Price'] = float(input("Price"))
            self.book_data['Quantity'] = int(input("Quantity:"))
            self.books[edit]=self.book_data

        with open("book.json","w") as file:
            json.dump(self.books,file)

        print("Book Updated Successfully!!!")

    def display_book(self):
        with open("book.json","r") as file:
            self.books = json.load(file)
            for k,v in self.books.items():
                print(k,"---->",v)