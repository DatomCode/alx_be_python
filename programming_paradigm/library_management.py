class Book:
# """A class representing a book with title, author, and availability."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        # """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        # """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        # """Check if the book is available."""
        return not self._is_checked_out
    

    class Library:
    # """A class representing a collection of books and operations on them."""

    
        def __init__(self):
            self._books = []

        def add_book(self, book):
            # """Add a book to the library collection."""
            self._books.append(book)

        def check_out_book(self, title):
            # """Check out a book by title if available."""
            for book in self._books:
                if book.title == title and book.is_available():
                    book.return_book()
                    return f"'{title}' has been returned."
                return f"'{title}' was not checked out."
                
        def list_available_books(self): 
            # """Print all available books in the library.""" 
            available = [book for book in self._books if book.is_available()]       
            if available: 
                for book in available: 
                    print(f"{book.title} by {book.author}") 
                else: print("No books available.")
