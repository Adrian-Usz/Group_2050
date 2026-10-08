from product import Product
from cart import ShoppingCart


class Customer:
    """Represents a custumer, and their shopping cart"""
    def __init__(self, customer_id: str, name: str):
        """Creates a customer with an ID, name, and empty shopping cart"""
        self.cart = ShoppingCart()
        self.customer_id = customer_id
        self.name = name

    def get_id(self):
        """returns the customer ID"""
        return self.customer_id

    def get_name(self):
        """Returns the customer name"""
        return self.name

    def get_cart(self):
        """Returns the customer's shopping cart"""
        return self.cart
