class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.myOrdDict = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.myOrdDict:
            return -1
        self.myOrdDict.move_to_end(key, last=True)
        return self.myOrdDict[key]
    def put(self, key: int, value: int) -> None:
        if key not in self.myOrdDict:
            if self.capacity <= 0:
                self.myOrdDict.popitem(last=False)
            else:
                self.capacity -= 1
        self.myOrdDict[key] = value
        self.myOrdDict.move_to_end(key, last=True)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
