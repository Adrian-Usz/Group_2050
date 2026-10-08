from customer import Customer
from product import Product

class Order:
  def __init__(self, order_id: str, customer: Customer, items: list[Product]) -> None:
    """ """
    self._order_id = order_id
    self._customer = customer
    self._items = list(items)
    self._status = "PENDING"
    
  def get_id(self) ->" str:
    return self._order_id

  def get_customer(self) -> Customer:
    """Return the customer who placed the order."""
    return self._customer

  def get_items(self) -> list[Product]:
    """Return a copy of the purchased product list."""
    return list(self._items)

  def get_status(self) -> str:
    """Return the current order status."""
    return self._status

  def set_status(self, status: str) -> None:
    """Set a valid status, raising ValueError for an unsupported value."""
    if status not in ("PENDING", "PROCESSING", "COMPLETED"):
      raise ValueError("Status must be PENDING, PROCESSING, or COMPLETED")
    self._status = status

  def calculate_total(self) -> float:
    """Return the total price of all purchased products."""
    total = 0.0
    for product in self._items:
      total += product.get_price()
    return total
    
