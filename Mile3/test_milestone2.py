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

    def test_stack(self):
        a = Stack()
        self.assertEqual(a.is_empty(), True)
        self.assertEqual(a.pop(), None)
        a.push(0)
        self.assertEqual(a.peek(), 0)
        a.push(1)
        self.assertEqual(a.size(), 2)
        self.assertEqual(a.pop(), 1)

    def test_order_queue(self):
        a = OrderQueue()
        self.assertEqual(a.is_empty(), True)
        self.assertEqual(a.dequeue(), None)
        a.enqueue(1)
        self.assertEqual(a.peek(), 1)
        a.enqueue(2)
        self.assertEqual(a.dequeue(), 1)

    def test_store_integ(self):
        store = Store()
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)
        alex = Customer("C100", "Alex")
        sam = Customer("C101", "Sam")
        store.add_customer(alex)
        store.add_customer(sam)

        alex_cart = alex.get_cart()
        sam_cart = sam.get_cart()

        alex_cart.add_product(mouse)
        alex_cart.add_product(keyboard)
        alex_order = store.checkout("C100")

        self.assertEqual(store.ordercounter, 1)

        sam_cart.add_product(headphones)
        sam_order = store.checkout("C101")

        first_order = store.process_next_order()
        self.assertEqual(first_order.get_status(), "PROCESSING")
        second_order = store.process_next_order()
        self.assertEqual(second_order.get_status(), "PROCESSING")

        self.assertEqual(store.get_order_history(), [second_order, first_order])
        

unittest.main()