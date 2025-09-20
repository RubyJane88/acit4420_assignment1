import pytest
import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bank_account import BankAccount
from src.savings_account import SavingsAccount
from src.checking_account import CheckingAccount

# Existing BankAccount tests (adjusted)
def test_bank_account_initialization():
    account = BankAccount("Ruby Jane")
    assert account.account_holder == "Ruby Jane"
    assert account.balance == 0.0

def test_bank_account_deposit():
    account = BankAccount("Ruby Jane")
    account.deposit(100.0)
    assert account.balance == 100.0

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

# Tests for SavingsAccount
def test_savings_account_initialization():
    account = SavingsAccount("Kairo", interest_rate=0.02)
    assert account.account_holder == "Kairo"
    assert account.balance == 0.0
    assert account.interest_rate == 0.02

def test_savings_account_apply_interest():
    account = SavingsAccount("Riri", balance=100.0, interest_rate=0.02)
    account.apply_interest()
    assert account.balance == 102.0  # 100 * (1 + 0.02)

def test_savings_account_inherit_deposit():
    account = SavingsAccount("Riri")
    account.deposit(200.0)
    assert account.balance == 200.0

# Tests for CheckingAccount
def test_checking_account_initialization():
    account = CheckingAccount("Raikko", transaction_fee=1.0)
    assert account.account_holder == "Raikko"
    assert account.balance == 0.0
    assert account.transaction_fee == 1.0

def test_checking_account_withdraw_with_fee():
    account = CheckingAccount("Kiki", balance=100.0, transaction_fee=1.0)
    account.withdraw(50.0)
    assert account.balance == 49.0  # 100 - 50 - 1

def test_checking_account_withdraw_insufficient_with_fee():
    account = CheckingAccount("Kiki", balance=50.0, transaction_fee=1.0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    account.withdraw(50.0)
    sys.stdout = sys.__stdout__
    assert "Insufficient funds for withdrawal and fee." in captured_output.getvalue()
    assert account.balance == 50.0