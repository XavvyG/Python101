from pdb import set_trace


class Budget():
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

    def __repr__(self):
        return f"The remaining balance of {self.type} is: {self.balance}"

    def withdraw(self, withdrawal):
        self.balance = self.balance - withdrawal
        return withdrawal

    def deposit(self, deposited):
        self.balance = self.balance + deposited
        return deposited