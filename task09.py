class User:
    def __init__(self, username, email, is_active=False):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print(f"Foydalanuvchi {self.username} faollashtirildi.")

    def deactivate(self):
        self.is_active = False
        print(f"Foydalanuvchi {self.username} bloklandi.")
        
user1 = User("shavkat_dev", "shavkat@gmail.com")
user1.activate()
user1.deactivate()