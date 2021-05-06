class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
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


omar = User("Omar", "Omardakka42@gmail.com")
haitham = User("Haitham", "Haitham@gmail.com")
ahmad = User("Ahmad", "Ahmad@gmail.com")
omar.make_deposit(150).make_deposit(50).make_deposit(
    300).make_withdrawal(200).display_user_balance()
haitham.make_deposit(500).make_deposit(1000).make_withdrawal(
    300).make_withdrawal(200).display_user_balance()
ahmad.make_deposit(700).make_withdrawal(500).make_withdrawal(
    300).make_withdrawal(200).display_user_balance()
omar.transfer_money(ahmad, 300)
ahmad.display_user_balance()
