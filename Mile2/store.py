from product import Product
from order import Order
from order_queue import OrderQueue
from stack import Stack

class Store:
    """Represents a store which manages all the products and customers"""
    def __init__(self):
        """Establishes a store that manages the products and customers"""
        self.products = []
        self.customers = []
        self.orders = []
        self.orderqueue = OrderQueue()
        self.orderhistory = Stack()
        self.ordercounter = 0

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
    def find_order(self, order_id: str) -> Order | None:
        for order in self.orders:
            if order.get_id() == order.id:
                return order
            return None
            
    def get_orders(self) -> list[Order]:
        return list(self.orders)

    def checkout(self, customer_id: str) -> Order | None:
        customer = self.find_customer(customer_id)
        if customer is None:
            return None
        cart = customer.get_cart()
        if cart.is_empty():
            return None
        self._order += 1
        order = Order(f"O{self._order_counter}", customer, cart.get_items())
        self.orders.append(order)
        self.orderqueue.enqueue(order)
        cart.clear()
        return order
    def process_next_order(self) -> Order | None:
        order = self.orderqueue.dequeue()
        if order is None:
            return None
        order.set_status("PROCESSING")
        self.order_history.push(order)
        return order

    def get_order_history(self) -> list[Order]:
        return self.order_history.to_list()
        

