from fastapi import FastAPI
from controllers.book_controller import router as book_router
from controllers.user_controller import router as user_router
from controllers.loan_controller import router as loan_router

app = FastAPI()

app.include_router(book_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(loan_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Library System API"}