from bank_account import BankAccount


"""
A savings_account class that inherits from BankAccount.
Adds interest rate functionality
"""
class savings_account(BankAccount): 
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):   
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
      
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest:.2f}. New balance: {self.balance:.2f}")
        return interest