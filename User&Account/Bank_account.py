class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self
    def yield_interest(self):
        intrest = self.balance*self.int_rate
        self.balance = self.balance + intrest
        return self

user1 = BankAccount (0.01, 0)
user2 = BankAccount (0.01, 0) 
# user1.deposit(100)
# user1.deposit(200)
# user1.deposit(300)
# user1.withdraw(100)
# user1.yield_interest()
# user1.display_account_info()
user1.deposit(500).deposit(100).deposit(100).withdraw(200).yield_interest().display_account_info()
user2.deposit(300).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

