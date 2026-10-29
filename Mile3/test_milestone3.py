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
from algorithms import *

class Test(unittest.TestCase):
    def test_catalogue_total(self):
        #2 tests, empty list, multiple products
        self.assertEqual(recursive_total_price([]), 0.0)
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        self.assertEqual(recursive_total_price([mouse, keyboard]), 89.98)
    def test_fewest_coins(self):
        #3 tests, amount 0, exact coin, larger amount
        self.assertEqual(fewest_coins([1, 5, 10], 0), 0)
        self.assertEqual(fewest_coins([1, 5, 10], 5), 1)
        self.assertEqual(fewest_coins([1, 5, 10, 25], 40), 3)
    def test_sorting(self):
        #4 tests, bubble, selection, insertion, already sorted, reverse order
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)
        b = [mouse, keyboard, headphones]
        a = [headphones, keyboard, mouse]
        bubble_sort(a)
        self.assertEqual(a, b)
        a = [headphones, keyboard, mouse]
        selection_sort(a)
        self.assertEqual(a, b)
        a = [headphones, keyboard, mouse]
        insertion_sort(a)
        self.assertEqual(a, b)
    def test_binary_search(self):
        #3 test, first item, middle item, not found
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)
        a = [mouse, keyboard, headphones]
        self.assertEqual(binary_search(a, "P100"), mouse)
        self.assertEqual(binary_search(a, "P101"), keyboard)
        self.assertEqual(binary_search(a, "P103"), -1)
    def test_store_integration(self):
        #3 tests, sort integration, binary lookup, change calculation
        store = Store()
        mouse = Product("P100", "Wireless Mouse", 29.99)
        keyboard = Product("P101", "Keyboard", 59.99)
        headphones = Product("P102", "Headphones", 39.99)
        for i in [headphones, keyboard, mouse]:
            store.add_product(i)
        self.assertEqual(store.binary_search_product("P101"), keyboard)    
        self.assertEqual(store.calculate_change([1, 5, 10, 25], 40), 3)
        store.bubble_sort_products()
        self.assertEqual(store.products, [mouse, keyboard, headphones])

unittest.main()