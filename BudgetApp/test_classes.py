from classes import Budget


def test_withdraw():
    category = Budget(10)
    category.withdraw(10)
    assert category.balance == 0

def test_deposit():
    category = Budget(10)
    category.deposit(10)
    assert category.balance == 20

def test_repr():
    category = Budget(10)
    assert category != "Balance remaining: 10"