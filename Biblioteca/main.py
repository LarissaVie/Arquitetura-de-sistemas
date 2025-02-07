from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import livros

app = FastAPI()

# Servir arquivos estáticos (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir roteadores
app.include_router(livros.router)