from sqlalchemy.orm import Session
from schemas import BookSchema
from config import SessionLocal
import crud

db = SessionLocal()

books = [{"title": "To Kill a Mockingbird", "author": "Harper Lee", "year_published": 1960},
         {"title": "Head First of javascript", "author": "George Orwell", "year_published": 1949},
         {"title": "One Hundred Years of Solitude",
             "author": "Gabriel Garcia Marquez", "year_published": 1967},
         {"title": "The Great Gatsby",
             "author": "F. Scott Fitzgerald", "year_published": 1925},
         {"title": "Pride and Prejudice", "author": "Jane Austen", "year_published": 1813}]

for book in books:
    book_obj = BookSchema(**book)
    crud.create_book(db, book_obj)

db.commit()
db.close()
