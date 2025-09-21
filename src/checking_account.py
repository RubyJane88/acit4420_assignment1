"""CheckingAccount class that inherits from BankAccount class.
    Adds withdraw functionality to include a transaction fee.
"""

from .bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, transaction_fee=1.0):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
         total_deduction = amount + self.transaction_fee
         if self.balance >= total_deduction: 
            super().withdraw(total_deduction)
            print(f"Withdrew ${amount:.2f} + ${self.transaction_fee:.2f} fee. New balance: ${self.balance:.2f}")
         else:
             print("Insufficient funds for withdrawal and fee.")
    

