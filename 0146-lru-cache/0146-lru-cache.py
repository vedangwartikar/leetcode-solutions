class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity # max capacity of cache
        self.cache = OrderedDict() # ensures LRU at  beginning and MRU at the end

    def get(self, key: int) -> int:
        if key not in self.cache: # key not present in cache
            return -1 # return -1
        val = self.cache[key] # get the value of the key from cache
        self.cache.move_to_end(key) # shift the key to the end of the cache (MRU)
        return val # return the value of the key

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # if key is already present
            del self.cache[key] # delete the key: value pair
        self.cache[key] = value # insert the updated key: value pair
        if len(self.cache) > self.capacity: # if the length of the cache exceeds capacity
            self.cache.popitem(last = False) # remove the key: value pair at the beginning (LRU)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)