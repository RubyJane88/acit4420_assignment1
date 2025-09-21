""" A simple BankAccount class to manage bank account operations.
    Base class responsible for handling deposits, withdrawals, and balance inquiries.

"""

class BankAccount:
    """Initialize a bank account with account holder's name, and initial balance."""
    def __init__(self,account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            
        else: 
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount: 
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else: 
                print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
                
    def account_info(self):
            return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


