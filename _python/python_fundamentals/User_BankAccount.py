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
    
class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(0.01, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        
user1 = User("Ahmed")
user1.make_deposit(100)
user1.make_withdrawal(20)
user1.display_user_balance() 