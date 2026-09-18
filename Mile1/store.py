class Store:
    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        for i in range(len(self.products)):
                if (self.products[i].get_id() == product.get_id()):
                    return False
        self.products.append(product)
        return True
    
    def find_product(self, product_id):
        for i in range(len(self.products)):
            if (self.products[i].get_id() == product_id):
                return self.products[i]
        return None
                 
    def add_customer(self, customer):
        for i in range(len(self.customers)):
                 if (self.customers[i].get_id() == customer.get_id()):
                    return False
        self.customers.append(customer)
        return True

    def find_customer(self, customer_id):
        for i in range(len(self.customers)):
            if (self.customers[i].get_id() == customer_id):
                return self.customers[i]
        return None
