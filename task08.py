class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Berilgan summani balansga qo'shadi."""
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        """Balans yetarli bo'lsa pul yechadi, aks holda ogohlantiradi."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Mablag' yetarli emas!")
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Berilgan summani balansga qo'shadi."""
        self.balance += amount
        print(f"Yangi balans: {self.balance}")

    def withdraw(self, amount):
        """Balans yetarli bo'lsa pul yechadi, aks holda ogohlantiradi."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Mablag' yetarli emas!")
def main():
    account = BankAccount("Ali", 1000)
    print(f"Hisob egasi: {account.owner}, Balans: {account.balance}")

    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)