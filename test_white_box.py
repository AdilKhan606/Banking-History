import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest

def test_deposit_error_branch():
    with pytest.raises(ValueError):
        deposit(500, -100)

def test_withdraw_negative():
    with pytest.raises(ValueError):
        withdraw(500, -50)

def test_transfer_negative_amount():
    with pytest.raises(ValueError):
        transfer(500, 300, -10)

def test_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-1000, 5, 2)

def test_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)
