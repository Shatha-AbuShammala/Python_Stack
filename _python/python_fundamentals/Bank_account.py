class BankAccount :
    def __init__ (self , int_rate , balance):
        self.int_rate = int_rate
        self.balance= balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance < amount :
            print ("no enough balance")
            self.balance -= 5
        else :
            self.balance -= amount
        return self    
    def display_account_info(self):
        print (f"{self.int_rate}:{self.balance}") 
        return self

    def yield_interest(self):
        if  self.balance > 0 :
            self.balance +=self.balance * self.int_rate
        return self    

account1 =BankAccount(.1 ,90)
account1.deposit(5).deposit(10).deposit(20).yield_interest().display_account_info()

account2 =BankAccount(.1 ,90)
account2.deposit(5).deposit(10).withdraw(20).withdraw(10)\
    .withdraw(10).withdraw(5).yield_interest().display_account_info()




