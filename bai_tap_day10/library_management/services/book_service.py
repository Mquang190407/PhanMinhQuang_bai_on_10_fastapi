from sqlalchemy.orm import Session
from models.book_model import BookModel
from schemas.book_schema import BookCreateSchema, BookUpdateSchema

def get_all_books(db: Session):
    return db.query(BookModel).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()

def create_book(db: Session, book_in: BookCreateSchema):
    new_book = BookModel(**book_in.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def update_book(db: Session, book_id: int, book_in: BookUpdateSchema):
    db_book = get_book_by_id(db, book_id)
    if db_book is None:
        return None

    update_data = book_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if db_book is None:
        return False

    db.delete(db_book)
    db.commit()
    return True
