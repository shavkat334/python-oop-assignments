class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        money = float(input("pul miqdori. "))
        self.balance += money
        result01 = print(f"sizning balansingizga {money} so'm pul qo'shildi!")
        result02 = print(f"sizning balansingiz {self.balance} so'm!")
        return result01, result02
    
    def withdraw(self):
        money = float(input("pul miqdori. "))
        if money > self.balance:
            result01 = print("balansingizda pul yetarli emas!")
            result02 = print(f"sizning balansingiz: {self.balance}!")
        else:
            self.balance -= money
            result03 = print(f"sizning balansingizdan {money} so'm pul yechildi!")
            result04 = print(f"sizning balansingiz {self.balance} so'm")

    
user01 = BankAccount("Ali", 50_000)

#user01.deposit()
user01.withdraw()