from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
import crud
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook,Response

router = APIRouter()



def get_db() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/create')
async def create(request:RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db,book = request.parameter)
    return Response(code=200, status="OK", message="Book created Successfully").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    books = crud.get_book(db,0,100)
    return Response(code=200, status="OK",message="Success Fetch All Data", result=books).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int, db:Session = Depends(get_db)):
    books = crud.get_book_by_id(db, id)
    return Response(code=200, status="OK", message="Success get Data", result=books).dict(exclude_none=True)

@router.post("/update")
async def update_book(request: RequestBook, db:Session=Depends(get_db)):
    books = crud.update_book(db, book_id=request.parameter.id,title=request.parameter.title, author=request.parameter.author, year_published=request.parameter.year_published)
    return Response(code=200, status="OK", message="Success update data", result=books)

@router.delete("/{id}")
async def delete(id:int, db:Session=Depends(get_db)):
    crud.remove_book(db, book_id=id)
    return Response(code=200, status="OK",message="Success delete data").dict(exclude_none=True)