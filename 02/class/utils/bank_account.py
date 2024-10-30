class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.interest_rate = 0.01

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, balance):
        self.balance -= balance

    def get_balance(self):
        return self.balance
    
    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate