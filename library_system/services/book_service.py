from dao.book_dao import BookDAO
from models.book import Book

class BookService:
    @staticmethod
    def get_all_books():
        return BookDAO.get_all_books()

    @staticmethod
    def get_book_by_id(book_id: int):
        return BookDAO.get_book_by_id(book_id)

    @staticmethod
    def add_book(book: Book):
        BookDAO.add_book(book)

    @staticmethod
    def update_book(book_id: int, updated_book: Book):
        return BookDAO.update_book(book_id, updated_book)

    @staticmethod
    def delete_book(book_id: int):
        BookDAO.delete_book(book_id)