from abc import ABC, abstractmethod

class Item(ABC):

    def __init__(self, title, author, is_rented=False):
        self.title = title  # Title of the item
        self.author = author  # Author of the item
        self.is_rented = is_rented  # Rental status (True for rented, False for available)

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def returning(self):
        pass

    @abstractmethod
    def listing(self):
        pass


class Book(Item):

    library = []  # Shared library of books

    def __init__(self, title, author, is_rented=False):
        super().__init__(title, author, is_rented)
        Book.library.append(self)  # Add book to the shared library

    def get_details(self):
        print(f"Book: {self.title} by {self.author}")

    def rent(self):
        if self.is_rented:
            print(f"Book: {self.title} is already rented, sorry.")
        else:
            self.is_rented = True
            print(f"Book: {self.title} rented successfully.")

    def returning(self):
        self.is_rented = False
        print(f"Thank you for returning the book: {self.title}")

    def listing(self):
        print("Library Listing:")
        for book in Book.library:
            status = "Rented" if book.is_rented else "Available"
            print(f"Book: {book.title} by {book.author}, Status: {status}")


# Test Code
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")

book1.rent()  # Rent the book
book1.rent()  # Try to rerent the book
book1.listing()  # List all books
book1.returning()  # Return the book
book1.listing()  # List again to confirm status