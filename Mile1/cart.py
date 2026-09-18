class ShoppingCart:
    """Shows the products in a given's customers shopping cart"""
    def __init__(self):
        """creates a new shopping cart with no items"""
        self.items = []

    def add_product(self, product: Product):
        """adds products to the shopping cart"""
        self.items.append(product)

    def remove_product(self, product_id: str):
        """removes a product by the ID, from the shopping cart, returns whether it was removed"""
        for i in range(len(self.items)):
            if self.items[i].get_id() == product_id:
                self.items.pop(i)
                return True
        return False

    def get_items(self):
        """returns the products current in the shopping cart"""
        return self.items

    def calculate_total(self):
        """Returns the total price of all products in the shopping cart"""
        total = 0.0
        for i in range(len(self.items)):
            total += self.items[i].get_price()
        return total

    def is_empty(self):
        """Returns whether or not the shopping cart is empty"""
        if self.items == []:
            return True
        else:
            return False
