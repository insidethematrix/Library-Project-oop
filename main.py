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
        return f"title: {self.title} author: {self.author} isbn: {self.isbn}"


class Library:
    """ Manages a collection of Book objects."""
    def __init__(self):
        """ Stores the books in library."""
        self.books={}

    def add_book(self,book):
        """ Adds the book object to the library. """
        if book.isbn in self.books:
                return False
            
        self.books[book.isbn] = book
        return True

    
    def list_books(self):
        """ Lists the information for all books. """
        return list(self.books.values())
    
    def find_book_by_isbn(self,isbn):
        """ Finds the book according to isbn. """
        return self.books.get(isbn)
    
    def remove_book(self, isbn):
        """ remove the books according to isbn """
        if isbn in self.books:
                book_to_remove = self.books[isbn]
                del self.books[isbn]
                return book_to_remove
        return None
        


if __name__=="__main__":
    my_library = Library()
    book1 = Book("Sefiller", "Victor Hugo", "978-605-332-401-8")
    book2 = Book("Suç ve Ceza", "Fyodor Dostoyevski", "978-605-332-237-3")
    book3 = Book("Fahrenheit 451", "Ray Bradbury", "978-605-375-316-0")

    # Add the books and check the results
    print("--- Adding books ---")
    for book in [book1, book2, book3]:
        if my_library.add_book(book):
            print(f"'{book.title}' was added successfully.")
        else:
            print(f"'{book.title}' could not be added (duplicate ISBN).")

    print("\n--- Listing all books ---")
    all_books = my_library.list_books()
    if not all_books:
        print("The library is empty.")
    else:
        for book in all_books:
            print(book.info())

    # finding book (exist)
    print("\n--- Finding an existing book ---")
    existing_book = my_library.find_book_by_isbn("978-605-332-237-3")
    if existing_book:
        print("Book found:")
        print(existing_book.info()) # .info() will return a text, print it out
    else:
        print("Book not found.")
        
    
    print("\n--- Finding a non-existing book ---")
    nonexisting_book = my_library.find_book_by_isbn("111-111-111-111-1")
    if nonexisting_book:
        print("Book found:")
        print(nonexisting_book.info()) 
    else:
        print("Book not found.")

    # Deleting book
    print("\n--- Removing a book ---")
    removed_book = my_library.remove_book("978-605-332-401-8") # Delete the Sefiller
    if removed_book:
        print(f"Successfully removed '{removed_book.title}'.")
    else:
        print("Book to remove was not found.")

    # List the latest status again
    print("\n--- Listing books after removal ---")
    all_books = my_library.list_books()
    if not all_books:
        print("The library is empty.")
    else:
        for book in all_books:
            print(book.info())