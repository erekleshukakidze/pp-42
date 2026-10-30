from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

Product1 = Product(name = "Car", price=60000, in_stock=True)
Product2 = Product(name = "Laptop", price=400, in_stock=False)
Product3 = Product(name= "Motorcycle", price=1000, in_stock=True)


print(Product1)
print(Product2)
print(Product3)