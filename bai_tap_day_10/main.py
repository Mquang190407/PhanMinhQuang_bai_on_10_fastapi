from fastapi import FastAPI
from database import Base, engine
from routers import book_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management API")
app.include_router(book_router.router)

@app.get("/")
def home():
    return {"message": "Library Management API"}
