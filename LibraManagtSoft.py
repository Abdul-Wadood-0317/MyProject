class Library:
    def __init__(self) :
        self.noBooks = 0
        self.book = []
    
    def addBook(self,book):
        self.book.append(book)
        self.noBooks = len(self.books)