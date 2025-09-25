# main.py
# This file contains a simple instance of a library management system.

class Book:
    """ Represents a book with a title, author and isbn. """
    def __init__(self, title, author, isbn):
        """ Initialize a book with its attributes.
        Args:
        title (str): The title of book.
        author (str): The Author of book.
        isbn (str): The unique isbn of book.
        """
        self.title=title
        self.author=author
        self.isbn=isbn
       

    def info(self):
        """ Prints the details of the book to the terminal. """
        print(f"title: {self.title} author: {self.author} isbn: {self.isbn}")


class Library:
    """ Manages a collection of Book objects."""
    def __init__(self):
        """ Stores the books in library."""
        self.books=[] 

    def add_book(self,book):
        """ Adds the book object to the library. """
        for i in self.books:
            if i.isbn == book.isbn:
                print(f"Book with ISBN {book.isbn} already exists in the library.")
                return
            
        self.books.append(book)
        print(f"'{book.title}' was added to the library.")

    
    def list_books(self):
        """ Lists the information for all books. """
        if not self.books:
            print("There are no books in the library yet.")
            return
        
        print("\n--- Books in the library ---")
        for book in self.books:
            book.info()
    
    def find_book_by_isbn(self,isbn):
        """ Finds the book according to isbn. """
        for book in self.books:
            if book.isbn==isbn:
                print("\n--- book was found ---")
                book.info()
                return
        print(f"\n'{isbn}' not found in the library.")
        return
    
    def remove_book(self, isbn):
        """ remove the books according to isbn """
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library")
                return
        print(f"No book with ISBN {isbn} found")


if __name__=="__main__":
    # Create an instance of our library
    my_library = Library()

    book1 = Book("Sefiller", "Victor Hugo", "978-605-332-401-8")
    book2 = Book("Suç ve Ceza", "Fyodor Dostoyevski", "978-605-332-237-3")
    book3 = Book("Fahrenheit 451", "Ray Bradbury", "978-605-375-316-0")

    # Add books and list them.
    my_library.list_books()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)
    my_library.list_books()

    my_library.find_book_by_isbn("978-605-332-237-3") # This one exists.
    my_library.find_book_by_isbn("123-456-789-0") # This one does not.

    my_library.remove_book("978-605-332-237-3")
    my_library.list_books()
