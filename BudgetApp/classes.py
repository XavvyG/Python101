class Budget():
    def __init__(self, balance):
        self.balance = balance
    
    def __repr__(self):
        return f"Balance remaining: {self.balance}"
        
    def deposit(self, deposited):
        self.balance += deposited
        return deposited

    def withdraw(self, withdrawn):
        self.balance -= withdrawn
        return withdrawn