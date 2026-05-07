class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(self.balance)

    def get_balance(self):
        return self.balance

accounts = [
    BankAccount("Ali", 1500),
    BankAccount("Vali", 2000),
    BankAccount("Sami", 3200),
    BankAccount("G'ani", 800),
    BankAccount("Hasan", 2500)
]

total_balance = 0
for account in accounts:
    total_balance += account.get_balance()

print(total_balance)