""" A simple BankAccount class to manage bank account operations.
    Base class responsible for handling deposits, withdrawals, and balance inquiries.

"""

class BankAccount:
    """Initialize a bank account with account number, holder's name, and initial balance."""
    def __init__(self,account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
            print(f"Insufficient funds for withdrawal of {amount}. Current balance: {self.balance}")
            return False

    def get_balance(self):
        return self.balance
    


