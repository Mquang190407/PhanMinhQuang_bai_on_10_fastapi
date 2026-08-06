from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.book_schema import BookCreateSchema, BookResponseSchema, BookUpdateSchema
from services import book_service

router = APIRouter(prefix="/api/v1/books", tags=["Book Controller"])

@router.get("", response_model=list[BookResponseSchema])
def get_all_books(db: Session = Depends(get_db)):
    return book_service.get_all_books(db)

@router.get("/{book_id}", response_model=BookResponseSchema)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book_by_id(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Sách không tồn tại trong hệ thống")
    return book

@router.post("", response_model=BookResponseSchema, status_code=201)
def create_book(book_in: BookCreateSchema, db: Session = Depends(get_db)):
    return book_service.create_book(db, book_in)

@router.put("/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book_in: BookUpdateSchema, db: Session = Depends(get_db)):
    book = book_service.update_book(db, book_id, book_in)
    if book is None:
        raise HTTPException(status_code=404, detail="Sách không tồn tại trong hệ thống")
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    result = book_service.delete_book(db, book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Sách không tồn tại trong hệ thống")
    return {"message": f"Đã xóa thành công sách ID {book_id}"}
