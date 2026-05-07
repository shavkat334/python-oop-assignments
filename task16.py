class Product:
    sale_parcent = 10.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_price(self) -> None:
        print(self.price - self.price * self.sale_parcent / 100)


p01 = Product('s22', 300)
p02 = Product('s23', 450)
p03 = Product('s24', 880)

Product.sale_parcent = 40

p02.show_price()
p03.show_price()