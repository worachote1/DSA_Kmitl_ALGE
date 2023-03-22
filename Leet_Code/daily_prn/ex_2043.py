class Bank(object):
    
    def __init__(self, balance):
        self.balance = balance
        
    def transfer(self, account1, account2, money):
        if(account1 > len(self.balance) or account2 > len(self.balance)):
            return False
        if(self.balance[account1-1] < money):
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account, money):
        if(account > len(self.balance)):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account, money):
        if(account > len(self.balance)):
            return False
        if(self.balance[account-1] < money):
            return False
        self.balance[account-1] -= money    
        return True