class Book:
    def __init__(self, title, author):
        self.name = title
        self.author = author

    def __str__(self):
        return f"Book: ({self.name} by {self.author})"
    

class Ebook(Book):
    def __init__(self, title, author, file_size):
        self.name = title
        self.author = author
        self.file_size = file_size


    def __str__(self):
        return f"EBook: ({self.name} by {self.author}, File Size: {self.file_size})"
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.name = title
        self.author = author
        self.page_count = page_count


    def __str__(self):
        return f"PrintBook: ({self.name} by {self.author}, Page Count: {self.page_count})"