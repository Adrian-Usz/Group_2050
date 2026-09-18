class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def remove_product(self, product_id: str):
        for i in range(len(self.items)):
            if self.items[i].get_id() == product_id:
                self.items.pop(i)
                return True
        return False

    def get_items(self):
        return self.items

    def calculate_total(self):
        total = 0.0
        for i in range(len(self.items)):
            total += self.items[i].get_price()
        return total

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False
