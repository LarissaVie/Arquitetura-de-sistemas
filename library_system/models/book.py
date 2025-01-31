from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    is_available: bool = True  # Indica se o livro está disponível para empréstimo