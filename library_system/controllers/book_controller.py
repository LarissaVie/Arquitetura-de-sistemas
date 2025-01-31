from fastapi import APIRouter, HTTPException
from models.book import Book
from services.book_service import BookService

router = APIRouter()

@router.get("/books")
def get_all_books():
    return BookService.get_all_books()

@router.get("/books/{book_id}")
def get_book(book_id: int):
    book = BookService.get_book_by_id(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/books")
def add_book(book: Book):
    BookService.add_book(book)
    return {"message": "Book added successfully"}

@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    if BookService.update_book(book_id, updated_book):
        return {"message": "Book updated successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    BookService.delete_book(book_id)
    return {"message": "Book deleted successfully"}