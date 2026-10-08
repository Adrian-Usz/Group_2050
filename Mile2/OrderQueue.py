from linked_list import LinkedList


class OrderQueue:
    """Store waiting items with first-in, first-out access."""

    def __init__(self) -> None:
        """Create an empty queue backed by a linked list."""
        self._items = LinkedList()

    def enqueue(self, item: object) -> None:
        """Add an item to the rear of the queue."""
        self._items.add_last(item)

    def dequeue(self) -> object | None:
        """Remove and return the front item, or None if empty."""
        return self._items.remove_first()

    def peek(self) -> object | None:
        """Return the front item without removing it, or None if empty."""
        return self._items.get_first()

    def is_empty(self) -> bool:
        """Return whether the queue contains no items."""
        return self._items.is_empty()

    def size(self) -> int:
        """Return the number of items in the queue."""
        return self._items.size()

