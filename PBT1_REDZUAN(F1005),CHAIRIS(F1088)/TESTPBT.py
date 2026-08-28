# -*- coding: utf-8 -*-
"""
TITLE : PROBLEM BASED TASK 1
NAME : 1) MUHAMMAD REDZUAN BIN PARSIKUN    MATRIX.NO : 1)03DDT21F1005
       2) CHAIRIS A/L PUM                              2)03DDT21F1088
CLASS: DDT4A

"""
import datetime

#create the class of book
class Book:
    
    # called every time an object is created from a class
    # def __init__ as a method
    def __init__(self, title, author, isbn, year_published):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year_published = year_published
    
    #Refer to this coding when admin want to add,search,display and delete books
    def __str__(self):
        return f"Title: {self.title}\n Author: {self.author}\n ISBN: {self.isbn}\n Year Published: {self.year_published}\n"

#create class of libraray
class Library:
    # def__init__ as a method
    def __init__(self):
        self.books = []
    
    # def add_book as a method
    def add_book(self, book):
        self.books.append(book)
    
    # def delete_book as a method
    def delete_book(self, book):
        self.books.remove(book)
    
    # def search_book as a method
    def search_book_by_title(self, title):
        matching_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                matching_books.append(book)
        return matching_books
    
   # def display_all_book as a method
    def display_all_books(self):
        if len(self.books) == 0:
            print("There are no books in the library.")
        else:
            for book in self.books:
                print(book)
                
    
#to read what admin create the file and directory handling
def read_library_file(file_path):
    library = Library()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                book_data = line.strip().split(',')
                book = Book(book_data[0], book_data[1], book_data[2], int(book_data[3]))
                library.add_book(book)
    except FileNotFoundError:
        pass
    return library

#to create the file and directory handling
def write_library_file(file_path, library):
    with open(file_path, 'w') as file:
        for book in library.books:
            file.write(f"{book.title},{book.author},{book.isbn},{book.year_published}\n")
            

            
def add_books():
            
                while True:
                    USER = input("Enter the book (yes) or quit?        :")
    
                    if USER == 'quit':
                        break
                 
                    elif USER == 'yes':
                        # ask user for file name
                        library_file_path = "library.txt"
                      
                        library = read_library_file(library_file_path)
                        title  = input("Enter the title of the book          :")
                        author = input("Enter the author of the book         :")
                        isbn   = input("Enter the ISBN of the book           :")
                        year_published = int(input("Enter the year the book was published:"))
                        book = Book(title, author, isbn, year_published)
                        library.add_book(book)
                        write_library_file(library_file_path, library)
                       
                        print("Book added to library.")
                        print("++---------------------------------------++")
                        continue
                   
def search_books():
                    
                  # search for a book by title
                 title = input("Enter the title of the book to search for: ")
                 matching_books = library.search_book_by_title(title)
                  
                 if len(matching_books) == 0:
                          print("\nNo matching books found.")
                      
                 else:
                          print("\nMatching books:")
                          for i, book in enumerate(matching_books):
                              print(f"{i+1}. {book}")
                      
                   
def menu():
    
    
  while True:
      
      print("++--------------------------------------++")
      print("+ 1 :  Add Books                         +")
      print("+ 2 :  Search Books                      +")
      print("+ 3 :  Display                           +")
      print("+ 4 :  Delete                            +")
      print("+ 5 :  Quit                              +")
      print("++--------------------------------------++")

      num = int(input("Insert The Number : "))               
      if num == 1:
                add_books()  
       
      elif num == 2:
                search_books()    
      elif num ==3:
                library.display_all_books()
      elif num ==4:
           title = input("Enter title of book to delete: ")
           book_list = library.search_book_by_title(title)
           if not book_list:
               print("Book not found")
           else:
               for i, book in enumerate(book_list):
                print(i+1, book)
                book_num = int(input("Enter book number to delete: "))
                book = book_list[book_num-1]
                library.delete_book(book)
                write_library_file("library.txt", library)
                print("Book deleted")
      elif num==5:
          print("Thank you !!!")
          break
      else:
          print("Wrong Input")
          break
          
#display output
          
print("++--------------------------------------++")
print("+     WELCOME TO PERPUSTAKAAN DESA       +")
print("++--------------------------------------++")

now = datetime.datetime.now()
print("Current date : ",now.strftime("%Y-%m-%d"))
print("Current time:",now.strftime("%H:%M:%S"))
print("Today is : ",now.strftime("%A"))
print()

#declare object as file
library_file_path = "library.txt"

#declare the object to read the file
library = read_library_file(library_file_path)

     
print("++--------------------------------------++")
print("+            Admin Platform              +")
print("++--------------------------------------++")
admin_Name = str(input("Admin's Name  : "))
#make admin use this password if wrong it will display wrong output
while True:
    admin_Password= str(input("Admin's Password  :  ")) 
    
    if admin_Password == "DESAPerpustakaan23_":
       menu()
       break
   
    elif admin_Password != "DESAPerpustakaan23_":
       print("Wrong Password , Please Try Again")
       continue
                       
