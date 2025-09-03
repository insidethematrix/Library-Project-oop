class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn


    def info(self):
        print(f"title: {self.title} author: {self.author} isbn: {self.isbn}")


class Library:
    def __init__(self):
        self.books=[]     # self.books = [] dediğinde, my_library nesnesine bir books özelliği ekleniyor ve bu özellik boş bir liste ([]) olarak başlatılıyor. 

    def add_book(self,book):
        self.books.append(book)
        print(f"'{book.title}' kütüphaneye eklendi.")
    
    def list_books(self):
        if not self.books:
            print("Kütüphanede henüz kitap bulunmuyor.")
            return
        
        print("\n--- Kütüphanedeki Kitaplar ---")
        for book in self.books:
            book.info()
    def find_book_by_isbn(self,isbn):
        for book in self.books:
            if book.isbn==isbn:
                print("\n--- book was found ---")
                book.info()
                return
        print(f"\n'{isbn}' not in library")
        return


my_library = Library()
book1 = Book("Sefiller", "Victor Hugo", "978-605-332-401-8")
book2 = Book("Suç ve Ceza", "Fyodor Dostoyevski", "978-605-332-237-3")
book3 = Book("Fahrenheit 451", "Ray Bradbury", "978-605-375-316-0")

my_library.list_books()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.list_books()
my_library.find_book_by_isbn("978-605-332-237-3") # Var olan bir kitap
my_library.find_book_by_isbn("123-456-789-0") 