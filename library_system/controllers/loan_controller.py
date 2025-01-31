from fastapi import APIRouter, HTTPException
from models.loan import Loan
from services.loan_service import LoanService

router = APIRouter()

@router.get("/loans")
def get_all_loans():
    return LoanService.get_all_loans()

@router.post("/loans")
def add_loan(loan: Loan):
    LoanService.add_loan(loan)
    return {"message": "Loan added successfully"}

@router.put("/loans/{loan_id}/return")
def return_book(loan_id: int):
    if LoanService.return_book(loan_id):
        return {"message": "Book returned successfully"}
    raise HTTPException(status_code=404, detail="Loan not found")