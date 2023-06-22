

class Account:

    def __init__(self, account_num, name, balance):
        self.num = account_num
        self.name = name
        self.bal = balance

class SavingsAccount(Account):

    def __init__(self, interest_rate):
        super().__init__()
        self.rate = interest_rate

    def apply_rate(self):
        self.bal*(1+self.rate)

class CheckingAccount(Account):

    def __init__(self, transaction_fee):
        super().__init__()
        self.fee = transaction_fee

class Bank:

    def __init__(self):
        self.accounts = []




