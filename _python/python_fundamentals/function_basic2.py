class User:
    def __init__ (self,name ,balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self, amount):
        self.balance -=amount
    def display_user_balance(self):    
        print(f"{self.name }: {self.balance}")
    def transfer_money(self, other_user , amount):
        self.balance -=amount
        other_user.balance +=amount

            

User1= User("Ahmed" , 100)
User1.make_withdrawal(10)
User1.display_user_balance()

User2=User("shatha", 20)
User1.transfer_money(User2 ,10)
User2.display_user_balance()


    

