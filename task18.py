class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"Mahsulot: {self.name}, Narxi: {self.price}")

products = [
    Product("Laptop", 1200, "Elektronika"),
    Product("Telefon", 800, "Elektronika"),
    Product("Monitor", 300, "Elektronika"),
    Product("Klaviatura", 50, "Aksessuar"),
    Product("Sichqoncha", 30, "Aksessuar"),
    Product("Printer", 400, "Texnika")
]

expensive_product = products[0]

for product in products:
    if product.price > expensive_product.price:
        expensive_product = product

expensive_product.info()