from sqlalchemy.orm import Session
from models import Book
from schemas import BookSchema

# Get all book Data
def get_book(db:Session, skip:int=0, limit: int=100):
    return db.query(Book).offset(skip).limit(limit).all()

# Get data by id
def get_book_by_id(db:Session, book_id:int):
    return db.query(Book).filter(Book.id == book_id).first()

# Create Book Data
def create_book(db:Session, book:BookSchema):
    books = Book(title=book.title,author=book.author, year_published = book.year_published)
    db.add(books)
    db.commit()
    db.refresh(books)
    return books

# Remove Book Data
def remove_book(db:Session, book_id:int):
    books = get_book_by_id(db=db,book_id=book_id)
    db.delete(books)
    db.commit()

# Update Book Data
def update_book(db:Session, book_id:int, title:str, author:str, year_published:int):
     books = get_book_by_id(db=db, book_id=book_id)
     books.title = title
     books.author = author
     books.year_published = year_published
     db.commit()
     db.refresh(books)
     return books


