class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate = 0.2, balance = 0)

    def make_deposit(self,amount):
        self.account.deposit += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: {}, Balance: {}".format(self.name, self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Interest Rate: {}, Balance: {}".format(self.int_rate, self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        return self
            



omar = User("Omar", "Omardakka42@gmail.com")
haitham = User("Haitham", "Haitham@gmail.com")
ahmad = User("Ahmad", "Ahmad@gmail.com")
# omar.account.deposit(100).account.deposit(500).account.deposit(400).account.withdraw(500).account.yield_interest().account.display_account_info()
# ibraheem.deposit(600).deposit(300).withdraw(100).withdraw(50).withdraw(200).withdraw(100).yield_interest().display_account_info()


omar.make_deposit(150).make_deposit(50).make_deposit(
    300).make_withdrawal(200).display_user_balance()
# haitham.make_deposit(500).make_deposit(1000).make_withdrawal(
#     300).make_withdrawal(200).display_user_balance()
# ahmad.make_deposit(700).make_withdrawal(500).make_withdrawal(
#     300).make_withdrawal(200).display_user_balance()
# omar.transfer_money(ahmad, 300)
# ahmad.display_user_balance()
