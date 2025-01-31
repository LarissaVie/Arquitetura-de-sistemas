from dao.loan_dao import LoanDAO
from models.loan import Loan
from datetime import datetime

class LoanService:
    @staticmethod
    def get_all_loans():
        return LoanDAO.get_all_loans()

    @staticmethod
    def get_loan_by_id(loan_id: int):
        return LoanDAO.get_loan_by_id(loan_id)

    @staticmethod
    def add_loan(loan: Loan):
        LoanDAO.add_loan(loan)

    @staticmethod
    def return_book(loan_id: int):
        loan = LoanDAO.get_loan_by_id(loan_id)
        if loan:
            loan.return_date = datetime.now()
            LoanDAO.update_loan(loan_id, loan)
            return True
        return False