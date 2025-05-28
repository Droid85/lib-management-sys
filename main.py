from pydantic import BaseModel
from abc import ABC, abstractmethod

class BookModel(BaseModel):
    title: str
    author: str
    year: int

class Publication(ABC):
    @abstractmethod
    def show_author(self):
        pass

class Book(Publication):
    def __init__(self, model: BookModel):
        self.model = model

    def __str__(self):
        return f"{self.model.title} by {self.model.author} in {self.model.year}"

    def show_author(self):
        return self.model.author

class Library:
    def __init__(self, book_list: list[str]):
        self.books = book_list
        self.current_book = 0

    def __iter__(self):
        self.current_book = 0

        return self

    def __next__(self):
        if self.current_book >= len(self.books):
            raise StopIteration

        b = self.books[self.current_book]
        self.current_book += 1

        return b

    def book_generator(self, author):
        for b in self.books:
            if b.author == author:
                yield b

    # def add2lib(self, b_title, b_author, b_year):
    #     def wrapper(*args, **kwargs):


book = Book(BookModel(title="1984", author="George Orwell", year=1949))

print(book)

myBooks = Library(['Math', 'Physics', 'Psychology'])

print(next(myBooks))
print(next(myBooks))
print(next(myBooks))

