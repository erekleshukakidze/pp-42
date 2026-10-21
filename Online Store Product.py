class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self,quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} piece(s) of {self.name}, remaining stock {self.stock}")
        else:
            print(f"Sorry, not enought stock available(available: {self.stock})")

laptop = Product("Laptop",4000, 15)

print(f"Shop {laptop.shop_name}")
print(f"Product: {laptop.name}, Initial stock: {laptop.stock}")
print("="*20)

laptop.sell(2)
laptop.sell(3)

print("="*20)
print(f"Current stock after sales: {laptop.stock}")

            
