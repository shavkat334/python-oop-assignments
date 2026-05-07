class Book:
    def __init__(self, title, author, is_read):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        return print(f"{self.title} Kitobi o'qilgan.")
    
    def status(self):
        if self.is_read == True:
            return print(f"{self.title} kitobi o'qilgan.")
        else:
            return print(f"{self.title} kitobi o'qilmagan.")
        
book01 = Book("Shum bola", "G'afur G'ulom", False)
book02 = Book("Jinlar Bazmi", "Abdulla Qodiriy", True)

book01.status()
book01.mark_as_read()


book02.status()
book02.mark_as_read()
