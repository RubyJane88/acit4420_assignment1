import pytest
import io
import sys

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        print("Insufficient funds")
        return False
    def get_balance(self):
        return self.balance


def test_bank_account_initialization():
    account = BankAccount("Ruby Jane")
    assert account.account_holder == "Ruby Jane"
    assert account.balance == 0.0

def test_bank_account_deposit(): 
    account = BankAccount("Ruby Jane")
    account.deposit(100.0)
    assert account.balance == 100.0
    assert account.account_holder == "Ruby Jane"

def test_bank_account_withdraw():
    account = BankAccount("Ruby Jane")
    account.deposit(100.0)
    account.withdraw(50.0)
    assert account.balance == 50.0
    
def test_bank_account_withdraw_insufficient_funds():
    account = BankAccount("Ruby Jane")
    account.deposit(50.0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    account.withdraw(100.0)
    sys.stdout = sys.__stdout__
    assert "Insufficient funds" in captured_output.getvalue()
    assert account.balance == 50.0