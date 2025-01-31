from typing import List
from models.book import Book

books = []

class BookDAO:
    @staticmethod
    def get_all_books() -> List[Book]:
        return books

    @staticmethod
    def get_book_by_id(book_id: int) -> Book:
        for book in books:
            if book.id == book_id:
                return book
        return None

    @staticmethod
    def add_book(book: Book):
        books.append(book)

    @staticmethod
    def update_book(book_id: int, updated_book: Book):
        for i, book in enumerate(books):
            if book.id == book_id:
                books[i] = updated_book
                return True
        return False

    @staticmethod
    def delete_book(book_id: int):
        global books
        books = [book for book in books if book.id != book_id]