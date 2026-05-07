class User:

    def __init__(self, username, email):

        self.username = username
        self.email = email
        self.is_active = True

u01 = User('shavkat334', 'shavkat@gmail.com',)

if u01.is_active:
    print('bu User active holatda')
else:
    print('bu User active holatda emas')
    