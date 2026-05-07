class BankAccount:
    def __init__(self, owner, balance):
        self.o = owner
        self.b = balance
    
    def deposit(self, amount):
        self.b += amount
        print(f"{self.o} hisobiga {self.b} qo\'shildi.")

    def withdraw(self, amount):
        if amount <= self.b:
            self.b -= amount
            print(f"{self.o} hisobidan {self.b} yechildi.")
        else:    
            print(f"{self.o} Mablag\' yetarli emas.")

    def show_balance(self):
        print(f"{self.o}ning yakuniy balans: {self.b}")

bank_a = BankAccount('Ali', 10_000)

bank_a.deposit(50_000)

bank_a.withdraw(20000_000)

bank_a.show_balance()