from typing import Optional
from pydantic import BaseModel, ConfigDict

class BookCreateSchema(BaseModel):
    title: str
    author: str
    price: float
    quantity: int = 0

class BookUpdateSchema(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

class BookResponseSchema(BookCreateSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)
