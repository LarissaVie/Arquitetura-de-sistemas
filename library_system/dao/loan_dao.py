from typing import List
from models.loan import Loan

loans = []

class LoanDAO:
    @staticmethod
    def get_all_loans() -> List[Loan]:
        return loans

    @staticmethod
    def get_loan_by_id(loan_id: int) -> Loan:
        for loan in loans:
            if loan.id == loan_id:
                return loan
        return None

    @staticmethod
    def add_loan(loan: Loan):
        loans.append(loan)

    @staticmethod
    def update_loan(loan_id: int, updated_loan: Loan):
        for i, loan in enumerate(loans):
            if loan.id == loan_id:
                loans[i] = updated_loan
                return True
        return False

    @staticmethod
    def delete_loan(loan_id: int):
        global loans
        loans = [loan for loan in loans if loan.id != loan_id]