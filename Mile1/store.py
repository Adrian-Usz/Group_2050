class Store:
    """Represents a store which manages all the products and customers"""
    def __init__(self):
        """Establishes a store that manages the products and customers"""
        self.products = []
        self.customers = []

    def add_product(self, product):
        """Adds a product if the ID does not already exist"""
        for i in range(len(self.products)):
                if (self.products[i].get_id() == product.get_id()):
                    return False
        self.products.append(product)
        return True
    
    def find_product(self, product_id):
        """Return the product if the ID exists, given the ID, or None if the ID is not found"""
        for i in range(len(self.products)):
            if (self.products[i].get_id() == product_id):
                return self.products[i]
        return None
                 
    def add_customer(self, customer):
        """Adds a customer that does not yet exist if the ID is not found"""
        for i in range(len(self.customers)):
                 if (self.customers[i].get_id() == customer.get_id()):
                    return False
        self.customers.append(customer)
        return True

    def find_customer(self, customer_id):
        """Returns the customer based off the ID, or returns None if the ID does not exist"""
        for i in range(len(self.customers)):
            if (self.customers[i].get_id() == customer_id):
                return self.customers[i]
        return None
