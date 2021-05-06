class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	
    	self.account_balance += amount

    def make_withdrawal(self, amount):	
    	self.account_balance -= amount

    def display_user_balance(self):
        print("User: {}, Balance: {}".format(self.name,self.account_balance))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

omar = User("Omar","Omardakka42@gmail.com")
haitham = User("Haitham","Haitham@gmail.com")
ahmad = User("Ahmad","Ahmad@gmail.com")

omar.make_deposit(150)
omar.make_deposit(50)
omar.make_deposit(300)
omar.make_withdrawal(200)
omar.display_user_balance()

haitham.make_deposit(500)
haitham.make_deposit(1000)
haitham.make_withdrawal(300)
haitham.make_withdrawal(200)
haitham.display_user_balance()

ahmad.make_deposit(700)
ahmad.make_withdrawal(500)
ahmad.make_withdrawal(300)
ahmad.make_withdrawal(200)
ahmad.display_user_balance()

omar.transfer_money(ahmad,300)
ahmad.display_user_balance()
