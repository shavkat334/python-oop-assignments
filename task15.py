class Product:

    def __init__(self, name: str, price: float, quantity: int, in_stock: bool = True):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.in_stock = in_stock


products = [
    Product('s22', 300, 19),
    Product('s23', 350, 10, False),
    Product('s24', 450, 0, False),
    Product('s25', 750, 5),
    Product('s26', 1250, 3),
]

total = 0
for product in products:
    if product.in_stock:
        total += product.price * product.quantity

print(total)