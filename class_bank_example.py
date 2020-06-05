class bankaccount:
    def __init__(self):#constructor
        self.balance=4000
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance

class sbi(bankaccount):
    def __init__(self,min_balance):
        bankaccount.__init__(self)
        self.min_balance=min_balance
    def withdraw(self,amount):
        if self.balance - amount < self.min_balance:
            print("Sorry, minimum balance must be maintained")
        else:
            print(bankaccount.withdraw(self,amounnt))
a=sbi(2000)
a.withdraw(1000)
