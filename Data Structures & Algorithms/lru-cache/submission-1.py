class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key -> (value, timestamp)
        self.order = []  # List to maintain the order of keys by usage

    def _update_access(self, key: int) -> None:
        """Update the order list to reflect access to a key."""
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key: int) -> int:
        if key in self.cache:
            value, _ = self.cache[key]
            # Update access order
            self._update_access(key)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and mark as most recently used
            self.cache[key] = (value, 0)
            self._update_access(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item
                lru_key = self.order.pop(0)  # Remove the first item from the list
                del self.cache[lru_key]
                
            # Insert the new key-value pair and mark as most recently used
            self.cache[key] = (value, 0)
            self.order.append(key)
