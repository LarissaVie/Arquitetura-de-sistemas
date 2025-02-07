from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from services.livro_service import (
    listar_livros,
    adicionar_livro,
    buscar_livro_por_id,
    editar_livro,
    deletar_livro,
)
from models.livro_model import Livro

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def listar_livros_view(request: Request):
    livros = listar_livros()
    return templates.TemplateResponse("index.html", {"request": request, "livros": livros})

@router.get("/adicionar", response_class=HTMLResponse)
async def adicionar_livro_form_view(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.get("/editar/{livro_id}", response_class=HTMLResponse)
async def editar_livro_form_view(request: Request, livro_id: int):
    livro = buscar_livro_por_id(livro_id)
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return templates.TemplateResponse("form.html", {"request": request, "livro": livro})

@router.post("/adicionar")
async def adicionar_livro_view(
    titulo: str = Form(...),
    autor: str = Form(...),
    ano_publicacao: int = Form(...),
    disponivel: bool = Form(False)
):
    novo_livro = Livro(
        id=len(listar_livros()) + 1,
        titulo=titulo,
        autor=autor,
        ano_publicacao=ano_publicacao,
        disponivel=disponivel
    )
    adicionar_livro(novo_livro)
    return RedirectResponse(url="/", status_code=303)

@router.post("/editar/{livro_id}")
async def editar_livro_view(
    livro_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    ano_publicacao: int = Form(...),
    disponivel: bool = Form(False)
):
    livro = buscar_livro_por_id(livro_id)
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    livro.titulo = titulo
    livro.autor = autor
    livro.ano_publicacao = ano_publicacao
    livro.disponivel = disponivel
    editar_livro(livro)
    return RedirectResponse(url="/", status_code=303)

@router.post("/deletar/{livro_id}")
async def deletar_livro_view(livro_id: int):
    deletar_livro(livro_id)
    return RedirectResponse(url="/", status_code=303)