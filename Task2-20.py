import json
from dataclasses import dataclass, asdict


@dataclass
class Product:
    name: str
    price: float
    in_stock: bool

Product1 = Product(name = "Car", price=60000, in_stock=True)
Product2 = Product(name = "Laptop", price=400, in_stock=False)
Product3 = Product(name= "Motorcycle", price=1000, in_stock=True)

products_list = [Product1, Product2, Product3]

products_dict_list = [asdict(p) for p in products_list]

json_string = json.dumps(products_dict_list, indent=4)
print(json_string)