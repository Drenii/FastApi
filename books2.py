from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS=[
    Book(1, 'Book 1', 'Author 1', 'Description 1', 5),
    Book(2, 'Book 2', 'Author 2', 'Description 2', 4),
    Book(3, 'Book 3', 'Author 3', 'Description 3', 3),
    Book(4, 'Book 4', 'Author 4', 'Description 4', 2),
    Book(5, 'Book 5', 'Author 5', 'Description 5', 1)

]

@app.get('/books')
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book=Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(new_book)
    