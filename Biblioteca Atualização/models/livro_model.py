from pydantic import BaseModel

class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: bool