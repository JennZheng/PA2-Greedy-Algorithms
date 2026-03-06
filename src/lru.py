from collections import OrderedDict

class LRU:
    def __init__(self, k):
        self.capacity = k
        # track order of keys based on when they were last inserted
        self. cache = OrderedDict()
    
    def request(self, r):
        # hit
        if r in self.cache:
            # move item to the end to mark as most recent
            self.cache.move_to_end(r)
            return "hit"
        
        # miss
        if len(self.cache) == self.capacity:
            # evict first item
            self.cache.popitem(last=False)
        
        # insert the new item as most recently used
        self.cache[r] = True
        return "miss"

def lru(k, m, r):
    cache = LRU(k)
    misses = 0

    for req in r:
        if cache.request(req) == "miss":
            misses += 1
    
    return misses
