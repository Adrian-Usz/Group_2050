class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add_product(self, product):
        self.cart.append(product)
    def remove_product(self, product_id):
        for i in range(len(self.cart)):
            if (self.cart[i].get_id() == product_id):
                self.cart.pop(i)
                return True
        return False
    def get_items(self):
        return self.cart
    def calculate_total(self):
        sum = 0.0
        for i in range(len(self.cart)):
            sum += self.cart[i].get_price()
        return sum
    def is_empty(self):
        if (self.cart == []):
            return True
        else:
            return False
