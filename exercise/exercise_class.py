# Library management System

"""
Create a library class infromation about books

Create Class of books
 -> Class contain title , author , availabilty (True/False) ✅

Create a class library ✅
-> Add a book into library ✅
-> Search for a book ✅
-> Checkout book by chaging its availability ✅
-> Display the available the book ✅
-> Display the list of all books
"""


class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True


class Library:
    def __init__(self):
        self.books: list[Books] = []

    def add_new_book(self, title, author):
        new_book = Books(title, author)
        self.books.append(new_book)
        print()
        print(f"{title} by {author} created")
        print()
        for item in self.books:
            print(item.title)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    pass
                    print(f"{title} by {book.author} available")
                else:
                    print(f"{title} by {book.author} checkout")

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"{title} by {book.author} checkout sucessfully")
                else:
                    print(f"{title} by {book.author} Not Available")
                return
        print(f"{title} is not in our library")

    def available_books(self):
        available_books = []
        for book in self.books:
            if book.is_available:
                available_books.append(book.title)
        print(available_books)

    def display_all(self):
        print(self.books)


def main():

    li = Library()

    while True:
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Checkout Book")
        print("4. Display available Book")
        print("5. Display all Book")
        print("6. Quit")

        option = input("Enter an option  ")

        if option == "1":
            book_name = input("Enter the book name  ").lower()
            author = input("Enter the author  ").lower()

            li.add_new_book(book_name, author)

        elif option == "2":
            book_name = input("Enter the book to search  ").lower()
            li.search_book(book_name)

        elif option == "3":
            book_name = input("Enter the book to checkout  ").lower()
            li.checkout_book(book_name)

        elif option == "4":
            li.available_books()

        elif option == "5":
            li.display_all()

        else:
            break
