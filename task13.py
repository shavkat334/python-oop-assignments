class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            print(self.title, "o'qilgan")
        else:
            print(self.title, "o'qilmagan")


b1 = Book("A", "a")
b2 = Book("B", "b")
b3 = Book("C", "c")
b4 = Book("D", "d")

b1.mark_as_read()
b3.mark_as_read()

b1.status()
b2.status()
b3.status()
b4.status()