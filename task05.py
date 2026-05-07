class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product1 = Product("Laptop", 12999.99, "Electronics", True)
product2 = Product("Smartwatch", 550.00, "Electronics", False)

print(f"Mahsulot nomi: {product1.name}, Narxi: {product1.price}")
print(f"Mahsulot nomi: {product2.name}, Narxi: {product2.price}")