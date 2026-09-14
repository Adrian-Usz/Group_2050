class Product:
    def __init__(self, product_id, name, price):
        if (type(product_id) == str):
            self.product_id = product_id
        else:
            raise TypeError
        
        if (type(name) == str):
            self.name = name
        else:
            raise TypeError

        if (type(price) == float):
            self.price = price
        else:
            raise TypeError

    def get_id(self):
        return self.product_id
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
