class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity} = ${self.price * self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product):
        if product.name in self.cart:
            self.cart[product.name].quantity += product.quantity
        else:
            self.cart[product.name] = product
        print(f"Added {product.name} to the cart.")

    def remove_product(self, product_name):
        if product_name in self.cart:
            del self.cart[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"{product_name} not found in the cart.")

    def calculate_total(self):
        Total = sum(product.price * product.quantity for product in self.cart.values())
        print("Total Cart Item Prize Is: ",Total)

    def show_cart(self):
        if not self.cart:
            print("The shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for product in self.cart.values():
                print(product)

product1 = Product("Laptop", 1000, 1)
product2 = Product("Phone", 500, 2)
product3 = Product("Headphones", 200, 1)

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.show_cart()
cart.remove_product("Phone")
cart.show_cart()
cart.calculate_total()

