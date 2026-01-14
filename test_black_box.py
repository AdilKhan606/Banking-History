import pytest
from bank_app import deposit, withdraw, transfer, calculate_interest, check_loan_eligibility

def test_deposit_positive():
    assert deposit(1000, 500) == 1500

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, 0)

def test_withdraw_valid():
    assert withdraw(1000, 300) == 700

def test_withdraw_more_than_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)

def test_transfer_success():
    from_bal, to_bal = transfer(1000, 500, 300)
    assert from_bal == 700
    assert to_bal == 800

def test_transfer_fail():
    with pytest.raises(ValueError):
        transfer(200, 500, 400)

def test_interest_calculation():
    assert round(calculate_interest(1000, 10, 2), 2) == 1210.0

def test_loan_eligibility():
    assert check_loan_eligibility(6000, 750) is True
