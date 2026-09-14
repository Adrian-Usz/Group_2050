class Store:
    def __init__(self):
        self.inventory = []
        self.shoppers = []

    def add_product(self, product):
        for i in range(len(self.inventory)):
                if (self.inventory[i].get_id() == product.get_id()):
                    return False
        self.inventory.append(product)
        return True
    
    def find_product(self, product_id):
        for i in range(len(self.inventory)):
            if (self.inventory[i].get_id() == product_id):
                return self.inventory[i]
        return None
                 
    def add_customer(self, customer):
        for i in range(len(self.shoppers)):
                 if (self.shoppers[i].get_id() == customer.get_id()):
                    return False
        self.inventory.append(customer)
        return True

    def find_customer(self, customer_id):
        for i in range(len(self.shoppers)):
            if (self.shoppers[i].get_id() == customer_id):
                return self.shoppers[i]
        return None
