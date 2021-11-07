from programs.classes import Budget

def test_withdraw():
    Budget(10)
    assert Budget.withdraw(10) == 0
    
def test_deposit():
    Budget(10)
    assert Budget.deposit(10) == 20
    
print(Budget(10))