import unittest

from cart import ShoppingCart
from customer import Customer
from linked_list import LinkedList
from node import Node
from order import Order
from order_queue import OrderQueue
from product import Product
from stack import Stack
from store import Store

class Test(unittest.TestCase):
    store = Store()
    mouse = Product("P100", "Wireless Mouse", 29.99)
    keyboard = Product("P101", "Keyboard", 59.99)
    headphones = Product("P102", "Headphones", 39.99)
    alex = Customer("C100", "Alex")
    sam = Customer("C101", "Sam")
    alex_cart = alex.get_cart()
    alex_cart.add_product(mouse)
    alex_cart.add_product(keyboard)
    alex_order = store.checkout("C100")
    sam_cart = sam.get_cart()
    sam_cart.add_product(headphones)
    sam_order = store.checkout("C101")
    first_order = store.process_next_order()
    second_order = store.process_next_order()

    def test_order(self):
        alex = Customer("C100", "Alex")
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        a = Order("order_id", alex, [mouse, keyboard])
        self.assertEqual(a.get_status(), a._status)
        self.assertEqual(a.get_status(), "PENDING")
        a.set_status("PROCESSING")
        self.assertEqual(a.get_status(), "PROCESSING")
        self.assertEqual(a.calculate_total(), 89.98)

    def test_linked_list(self):
        a = LinkedList()
        a.add_first('a')
        self.assertEqual(a.get_first(), 'a')
        a.add_last('b')
        self.assertEqual(a.size(), 2)
        a.remove_first()
        self.assertEqual(a.get_first(), 'b')
        b = LinkedList()
        self.assertEqual(b.get_first(), None)

        

unittest.main()