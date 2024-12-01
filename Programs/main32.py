class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def getBookInfo(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

book = Book("1984", "George Orwell", 1949)
print(book.getBookInfo())
