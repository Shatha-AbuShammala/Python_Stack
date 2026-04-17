class BankAccount :
    def __init__ (self , int_rate , balance):
        self.int_rate = int_rate
        self.balance= balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance < amount :
            print ("no enough balance")
            self.balance -= 5
        else :
            self.balance -= amount
    def display_account_info(self):
        print (f"{self.int_rate}:{self.balance}") 

    def yield_interest(self):
        if  self.balance > 0 :
            self.balance +=self.balance * self.int_rate

BankAccount1 =BankAccount(.1 ,90)
BankAccount1.deposit(5)
BankAccount1.yield_interest()
BankAccount1.display_account_info()



