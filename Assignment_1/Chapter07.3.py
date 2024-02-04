class Account:
    def __init__(self,id=0,balance=100.0,annualInterestRate=0.0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance=balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def setAnnualInterestRate(self,rate):
        self.__annualInterestRate=rate
    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12/100
    def getMonthlyInterest(self):
        return self.getMonthlyInterestRate()*self.__balance
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Invalid Withdrawl Amount")
    def deposit(self,amount):
        if amount>0 :
            self.__balance+=amount
        else:
            print("Invalid Deposit Amount")

#Test
acc=Account(1122,20000,4.5)

acc.withdraw(2500)
acc.deposit(3000)

print("Account ID: ",acc.getId())
print("Balance: ",acc.getBalance())
print("Monthly Interest Rate:",acc.getMonthlyInterestRate())
print("Monthly Interest: ",acc.getMonthlyInterest())