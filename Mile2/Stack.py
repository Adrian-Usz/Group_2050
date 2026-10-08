from linked_list import LinkedList


class Stack:
    """Store items with last-in, first-out access."""

    def __init__(self) -> None:
        """Create an empty stack backed by a linked list."""
        self._items = LinkedList()

    def push(self, item: object) -> None:
        """Add an item to the top of the stack."""
        self._items.add_first(item)

    def pop(self) -> object | None:
        """Remove and return the top item, or None if empty."""
        return self._items.remove_first()

    def peek(self) -> object | None:
        """Return the top item without removing it, or None if empty."""
        return self._items.get_first()

    def is_empty(self) -> bool:
        """Return whether the stack contains no items."""
        return self._items.is_empty()

    def size(self) -> int:
        """Return the number of items in the stack."""
        return self._items.size()

    def to_list(self) -> list[object]:
        """Return a new list from top to bottom without modifying the stack."""
        return list(self._items)

