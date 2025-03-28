from models.livro_model import Livro

# Simulação de banco de dados em memória
livros_db = []

def listar_livros():
    return livros_db

def adicionar_livro(livro: Livro):
    livros_db.append(livro)

def buscar_livro_por_id(livro_id: int):
    return next((livro for livro in livros_db if livro.id == livro_id), None)

def editar_livro(livro_atualizado: Livro):
    for i, livro in enumerate(livros_db):
        if livro.id == livro_atualizado.id:
            livros_db[i] = livro_atualizado
            break

def deletar_livro(livro_id: int):
    global livros_db
    livros_db = [livro for livro in livros_db if livro.id != livro_id]