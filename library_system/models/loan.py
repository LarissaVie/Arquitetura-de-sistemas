from pydantic import BaseModel
from datetime import datetime

class Loan(BaseModel):
    id: int
    book_id: int
    user_id: int
    loan_date: datetime
    return_date: datetime = None  # Data de devolução (None se ainda não devolvido)