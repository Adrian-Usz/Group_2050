class Customer:
    def __init__(self, customer_id, name):
        self.cart = ShoppingCart()

        if (type(customer_id) == str):
            self.customer_id = customer_id
        else:
            raise TypeError

        if (type(name) == str):
            self.name = name
        else:
            raise TypeError

    def get_id(self):
        return self.customer_id

    def get_name(self):
        return self.name

    def get_cart(self):
        return self.cart
    
