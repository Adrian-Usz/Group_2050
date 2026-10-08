class Product:
    """This represents a product sold by the store"""
    def __init__(self, product_id: str, name: str, price: float):
        """This creates a product with an ID, listed as a string, a name (also a string), and price (float)"""
        
        self.product_id = product_id
        self.name = name
        self.price = price

    
    def get_id(self):
        """returns the product ID"""
        return self.product_id
        
    def get_name(self):
        """returns the product name"""
        return self.name
        
    def get_price(self):
        """returns the price of the product"""
        return self.price
