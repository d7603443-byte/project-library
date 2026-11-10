from library.input import *
from library.data import *

def chose_number():
    while True:
        chose = menu()
        if chose == "8":
                return"have a nice day"
            
        if chose  not in["1", "2", "3", "4", "5", "6", "7"]:
            print("try again")

        if chose == "1":
            display_books()

        if chose =="2":
            search_book()

        if chose == "3":
           add_book()

        if chose =="4":
             borrow = input("enter name the book")
             borrow_book(borrow)
            

        if chose =="5":
            back = input("enter name the book")
            return_book(back)
        
        if chose =="6":
            get_available_books()
            
        if chose =="7":
            author = input("enter tae author")
            get_books_by_author(author)
                


def display_books():
    for book in books:
        print(book)

def search_book():
    name = input("enter your book anme")
    for book in books:
         if name in book["name"]:
              print( book)
    print( "404, not found")
         

def add_book():
        try:
            name = input("enter name book")
            author =input("enter author book")
            year = input ("enter year book")
            year = int(year)
            if year < 0:
                raise ValueError ("the number must be positive")
            books.append (f" id: {get_next_book_id(books)}, name: {name}, author:{author}, year: {year}, available: True")
            print(books)
        except ValueError, TypeError:
            print("try again")
            
        
 
def borrow_book(borrow):
    for book in books:
        if book["name"] == borrow:
            if book["available"] == False:
                print ("The book has already been borrowed. ")
            print("Book borrowed successfully ")
            book["available"] = False
    print ("404, not found")
    return menu()

def return_book( back):
    for book in books:
        if book["name"] == back:
            if book["available"] == True:
                return ("The book has already been returned.. ")
            print("The book was returned successfully. ")
            book["available"] = False
            return menu()
    print ("404, not found")
    

def get_available_books():
    free = []
    for book in books:
        if book["available"] == True:
            free.append(book["name"])
        if free == []:
            print ("404, not found")
            return menu()
    print("The book was returned successfully. ")
    print(free)
    
    


def get_books_by_author(author):
    for book in books:
        if author in book["author"]:
            print(book)
    print("404, not found")
    
             

def get_next_book_id(books):
    return len(books) + 1
    


                
                    
                
        
    
        
    




    