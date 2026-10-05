class LRUCache:
    class Node:
        def __init__(self, key, value,):
            self.value = value
            self.key = key
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = self.Node(0, 0)
        self.MRU = self.Node(0, 0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        self.cache: Dict[int, "Node"] = {}

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        node.next = self.MRU
        node.prev= self.MRU.prev
        node.prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        # edge case: the key doesn't exist in cache
        if key not in self.cache:
            return -1
        # recover the item
        item = self.cache[key].value
        # move the node to the back of the line
        self._remove(self.cache[key])
        self._add(self.cache[key])
        return item

    def put(self, key: int, value: int) -> None:
        # if the item doesn't exist
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = self.Node(key, value)
        self._add(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.LRU.next
            self._remove(lru)
            del self.cache[lru.key]