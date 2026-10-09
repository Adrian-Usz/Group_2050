from node import Node


class LinkedList:
    """Store items in connected nodes while tracking head, tail, and size."""

    def __init__(self) -> None:
        """Create an empty linked list."""
        self._head = None
        self._tail = None
        self._count = 0

    def add_first(self, item: object) -> None:
        """Insert an item at the front in O(1) time."""
        node = Node(item, self._head)
        self._head = node
        if self._tail is None:
            self._tail = node
        self._count += 1

    def add_last(self, item: object) -> None:
        """Insert an item at the rear in O(1) time using the tail reference."""
        node = Node(item)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
            self._tail = node
        self._count += 1

    def remove_first(self) -> object | None:
        """Remove and return the front item, or None if empty."""
        if self._head is None:
            return None
        item = self._head.data
        self._head = self._head.next
        self._count -= 1
        if self._head is None:
            self._tail = None
        return item

    def get_first(self) -> object | None:
        """Return the front item without removing it, or None if empty."""
        if self._head is None:
            return None
        return self._head.data

    def is_empty(self) -> bool:
        """Return whether the list contains no items."""
        return self._count == 0

    def size(self) -> int:
        """Return the number of stored items in O(1) time."""
        return self._count

    def __iter__(self) -> Iterator[object]:
        """Yield items from front to rear without changing the list."""
        current = self._head
        while current is not None:
            yield current.data
            current = current.next

