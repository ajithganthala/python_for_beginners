class bankaccount:
    def __init__(self):#constructor
        self.balance=0
    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
e=bankaccount()
print(e.deposit(5000))  #5000
print(e.withdraw(1000)) #1000
