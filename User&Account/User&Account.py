from Bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # other methods
    def make_deposit(self, amount):
        self.account.make_deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)		# or access its attributes
    def make_withdraw(self, amount):
        self.account.make_withdraw(100)		# we can call the BankAccount instance's methods

    # def example_method(self):
    #     self.account.deposit(100)		# we can call the BankAccount instance's methods

    
print(BankAccount.display_account_info)		# or access its attributes


    




