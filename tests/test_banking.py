import pytest
import io
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bank_account import BankAccount
from src.savings_account import SavingsAccount
from src.checking_account import CheckingAccount

# Fixtures for reusable accounts (avoids repetition)
@pytest.fixture
def base_account():
    return BankAccount("Ruby Jane")

@pytest.fixture
def savings_account():
    return SavingsAccount("Kairo", interest_rate=0.02)

@pytest.fixture
def checking_account():
    return CheckingAccount("Raikko", transaction_fee=1.0)

# BankAccount Tests
def test_bank_account_initialization(base_account):
    assert base_account.account_holder == "Ruby Jane"
    assert base_account.balance == 0.0

def test_bank_account_deposit(base_account):
    base_account.deposit(100.0)
    assert base_account.balance == 100.0

def test_bank_account_withdraw(base_account):
    base_account.deposit(100.0)
    base_account.withdraw(50.0)
    assert base_account.balance == 50.0

def test_bank_account_withdraw_insufficient_funds(base_account):
    base_account.deposit(50.0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    base_account.withdraw(100.0)
    sys.stdout = sys.__stdout__
    assert "Insufficient funds" in captured_output.getvalue()
    assert base_account.balance == 50.0

def test_bank_account_account_info(base_account):
    base_account.deposit(100.0)
    info = base_account.account_info()
    assert "Ruby Jane" in info
    assert "$100.00" in info 

# SavingsAccount Tests
def test_savings_account_initialization(savings_account):
    assert savings_account.account_holder == "Kairo"
    assert savings_account.balance == 0.0
    assert savings_account.interest_rate == 0.02

def test_savings_account_apply_interest_initial(savings_account):
    savings_account.apply_interest()
    assert savings_account.balance == pytest.approx(0.0, abs=0.01)

def test_savings_account_apply_interest(savings_account):
    savings_account.deposit(100.0)  # Use inherited deposit
    savings_account.apply_interest()
    assert savings_account.balance == pytest.approx(102.0, abs=0.01)

def test_savings_account_inherit_deposit(savings_account):
    savings_account.deposit(200.0)
    assert savings_account.balance == 200.0

@pytest.mark.parametrize("initial_balance, expected", [(100.0, 102.0), (0.0, 0.0)])
def test_savings_account_various_balances(initial_balance, expected):
    account = SavingsAccount("Test", balance=initial_balance, interest_rate=0.02)
    account.apply_interest()
    assert account.balance == pytest.approx(expected, abs=0.01)

# CheckingAccount Tests
def test_checking_account_initialization(checking_account):
    assert checking_account.account_holder == "Raikko"
    assert checking_account.balance == 0.0
    assert checking_account.transaction_fee == 1.0

def test_checking_account_withdraw_with_fee(checking_account):
    checking_account.deposit(100.0)  # Use inherited deposit
    checking_account.withdraw(50.0)
    assert checking_account.balance == pytest.approx(49.0, abs=0.01)

def test_checking_account_withdraw_insufficient_with_fee(checking_account):
    checking_account.deposit(50.0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    checking_account.withdraw(50.0)
    sys.stdout = sys.__stdout__
    assert "Insufficient funds for withdrawal and fee." in captured_output.getvalue()
    assert checking_account.balance == 50.0



