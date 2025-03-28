from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Configuração dos templates e arquivos estáticos
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Constantes
MULTA_DIARIA = 2.00  # R$ por dia de atraso
DIAS_EMPRESTIMO = 7  # Dias padrão para empréstimo

# Modelos de dados
class Livro(BaseModel):
    id: int
    titulo: str
    autor: str
    editora: str
    ano_publicacao: int
    genero: str
    quantidade: int

class Usuario(BaseModel):
    id: int
    nome: str
    email: str

class Emprestimo(BaseModel):
    id: int
    livro_id: int
    usuario_id: int
    data_emprestimo: datetime
    data_devolucao: datetime
    devolvido: bool = False

# "Banco de dados" em memória
db = {
    "livros": [],
    "usuarios": [],
    "emprestimos": []
}

# Funções auxiliares
def get_livro(livro_id: int) -> Optional[Livro]:
    return next((l for l in db["livros"] if l.id == livro_id), None)

def get_usuario(usuario_id: int) -> Optional[Usuario]:
    return next((u for u in db["usuarios"] if u.id == usuario_id), None)

def get_emprestimo(emprestimo_id: int) -> Optional[Emprestimo]:
    return next((e for e in db["emprestimos"] if e.id == emprestimo_id), None)

def calcular_multa(emprestimo: Emprestimo) -> float:
    if not emprestimo.devolvido and datetime.now() > emprestimo.data_devolucao:
        dias_atraso = (datetime.now() - emprestimo.data_devolucao).days
        return dias_atraso * MULTA_DIARIA
    return 0.0

# Rotas para Livros (RF01-RF04)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/livros", response_class=HTMLResponse)
async def listar_livros(
    request: Request,
    titulo: str = None,
    autor: str = None,
    genero: str = None
):
    livros_filtrados = db["livros"]
    
    if titulo:
        livros_filtrados = [l for l in livros_filtrados if titulo.lower() in l.titulo.lower()]
    if autor:
        livros_filtrados = [l for l in livros_filtrados if autor.lower() in l.autor.lower()]
    if genero:
        livros_filtrados = [l for l in livros_filtrados if genero.lower() in l.genero.lower()]
    
    return templates.TemplateResponse("livros/listar.html", {
        "request": request,
        "livros": livros_filtrados,
        "filtros": {"titulo": titulo, "autor": autor, "genero": genero}
    })

@app.get("/livros/novo", response_class=HTMLResponse)
async def formulario_livro(request: Request):
    return templates.TemplateResponse("livros/formulario.html", {
        "request": request,
        "livro": None
    })

@app.get("/livros/{livro_id}/editar", response_class=HTMLResponse)
async def editar_livro_form(request: Request, livro_id: int):
    livro = get_livro(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return templates.TemplateResponse("livros/formulario.html", {
        "request": request,
        "livro": livro
    })

@app.post("/livros")
async def criar_livro(
    titulo: str = Form(...),
    autor: str = Form(...),
    editora: str = Form(...),
    ano_publicacao: int = Form(...),
    genero: str = Form(...),
    quantidade: int = Form(...)
):
    novo_livro = Livro(
        id=len(db["livros"]) + 1,
        titulo=titulo,
        autor=autor,
        editora=editora,
        ano_publicacao=ano_publicacao,
        genero=genero,
        quantidade=quantidade
    )
    db["livros"].append(novo_livro)
    return RedirectResponse(url="/livros", status_code=303)

@app.post("/livros/{livro_id}")
async def atualizar_livro(
    livro_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    editora: str = Form(...),
    ano_publicacao: int = Form(...),
    genero: str = Form(...),
    quantidade: int = Form(...)
):
    livro = get_livro(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    livro.titulo = titulo
    livro.autor = autor
    livro.editora = editora
    livro.ano_publicacao = ano_publicacao
    livro.genero = genero
    livro.quantidade = quantidade
    
    return RedirectResponse(url="/livros", status_code=303)

@app.post("/livros/{livro_id}/remover")
async def remover_livro(livro_id: int):
    db["livros"] = [l for l in db["livros"] if l.id != livro_id]
    return RedirectResponse(url="/livros", status_code=303)

# Rotas para Usuários
@app.get("/usuarios", response_class=HTMLResponse)
async def listar_usuarios(request: Request):
    return templates.TemplateResponse("usuarios/listar.html", {
        "request": request,
        "usuarios": db["usuarios"]
    })

@app.post("/usuarios")
async def criar_usuario(nome: str = Form(...), email: str = Form(...)):
    novo_usuario = Usuario(
        id=len(db["usuarios"]) + 1,
        nome=nome,
        email=email
    )
    db["usuarios"].append(novo_usuario)
    return RedirectResponse(url="/usuarios", status_code=303)

# Rotas para Empréstimos (RF05-RF07)
@app.get("/emprestimos", response_class=HTMLResponse)
async def listar_emprestimos(request: Request):
    emprestimos_com_info = []
    for emp in db["emprestimos"]:
        livro = get_livro(emp.livro_id)
        usuario = get_usuario(emp.usuario_id)
        emprestimos_com_info.append({
            "emprestimo": emp,
            "livro": livro,
            "usuario": usuario,
            "multa": calcular_multa(emp)
        })
    
    return templates.TemplateResponse("emprestimos/listar.html", {
        "request": request,
        "emprestimos": emprestimos_com_info,
        "livros": [l for l in db["livros"] if l.quantidade > 0],
        "usuarios": db["usuarios"]
    })

@app.post("/emprestimos")
async def criar_emprestimo(
    livro_id: int = Form(...),
    usuario_id: int = Form(...),
    dias_emprestimo: int = Form(DIAS_EMPRESTIMO)
):
    livro = get_livro(livro_id)
    usuario = get_usuario(usuario_id)
    
    if not livro or not usuario:
        raise HTTPException(status_code=404, detail="Livro ou usuário não encontrado")
    
    if livro.quantidade <= 0:
        raise HTTPException(status_code=400, detail="Livro não disponível para empréstimo")
    
    data_emprestimo = datetime.now()
    data_devolucao = data_emprestimo + timedelta(days=dias_emprestimo)
    
    novo_emprestimo = Emprestimo(
        id=len(db["emprestimos"]) + 1,
        livro_id=livro_id,
        usuario_id=usuario_id,
        data_emprestimo=data_emprestimo,
        data_devolucao=data_devolucao
    )
    
    db["emprestimos"].append(novo_emprestimo)
    livro.quantidade -= 1
    
    return RedirectResponse(url="/emprestimos", status_code=303)

@app.post("/emprestimos/{emprestimo_id}/devolver")
async def devolver_emprestimo(emprestimo_id: int):
    emprestimo = get_emprestimo(emprestimo_id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado")
    
    livro = get_livro(emprestimo.livro_id)
    if livro:
        livro.quantidade += 1
    
    emprestimo.devolvido = True
    return RedirectResponse(url="/emprestimos", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)