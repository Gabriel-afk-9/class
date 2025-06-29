class BookUnavailableError(Exception):
    pass

class BookNotBorrowedError(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available"

    def __str__(self):
        return f'{self.title} by {self.author} - Status: {self.status}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, title):
        book = self.find_book(title)
        if book:
            if book.status == "available":
                book.status = "borrowed"
            else:
                raise BookUnavailableError(f'O livro "{title}" não está disponível para empréstimo.')
        else:
            print(f'O livro "{title}" não foi encontrado.')

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            if book.status == "borrowed":
                book.status = "available"
            else:
                raise BookNotBorrowedError(f'O livro "{title}" não foi emprestado.')
        else:
            print(f'O livro "{title}" não foi encontrado.')

    def list_available_books(self):
        available_books = []

        for book in self.books:
            if book.status == "available":
                available_books.append(book)
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("Não há livros disponíveis para empréstimo.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

if __name__ == "__main__":
    library = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Livros disponíveis para empréstimo:")
    library.list_available_books()

    print("\nEmprestando '1984'...")
    library.lend_book("1984")
    library.list_available_books()

    print("\nDevolvendo '1984'...")
    library.return_book("1984")
    library.list_available_books()

    try:
        print("\nTentando emprestar '1984' novamente...")
        library.lend_book("1984")
    except BookUnavailableError as e:
        print(e)

    try:
        print("\nTentando devolver '1984' novamente...")
        library.return_book("1984")
    except BookNotBorrowedError as e:
        print(e)
