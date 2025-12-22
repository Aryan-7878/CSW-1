class Product:
   
    total_products_sold = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Product.total_products_sold += amount
            print(f"{amount} units of {self.name} sold.")
        else:
            print("Not enough stock available.")

    
    @classmethod
    def get_total_products_sold(cls):
        return cls.total_products_sold



p1 = Product("Laptop", 50000, 10)
p2 = Product("Mobile", 20000, 20)


p1.sell_product(3)
p2.sell_product(5)


print("Remaining quantity of Laptop:", p1.quantity)
print("Remaining quantity of Mobile:", p2.quantity)


print("Total products sold:", Product.get_total_products_sold())