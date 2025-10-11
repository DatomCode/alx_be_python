class Book:
    def __init__(self, title, author):
        self.name = title
        self.author = author

    def __str__(self):
        return f"Book: ({self.name} by {self.author})"
    

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


    def __str__(self):
        return f"EBook: ({self.name} by {self.author}, File Size: {self.file_size})"
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


    def __str__(self):
        return f"PrintBook: ({self.name} by {self.author}, Page Count: {self.page_count})"
    



class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"✅ '{book.title}' added to the library.")

    def list_books(self):
        if not self.books:
            print("📚 The library is empty.")
            return
        print("\n📖 Library Collection:\n" + "-" * 30)
        for book in self.books:
            print(book.get_info())
        print("-" * 30)