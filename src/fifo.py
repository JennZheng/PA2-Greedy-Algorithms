from collections import deque

class FIFO:
    def __init__(self, k):
        self.capacity = k
        self.cache = set()
        self.queue = deque() # track arrival order
    
    def request(self, item):
        # hit
        if item in self.cache:
            return "hit"
        
        # miss
        if len(self.cache) == self.capacity:
            # cahce is full so evict the oldest/the one at the front
            oldest = self.queue.popleft()
            self.cache.remove(oldest)
        
        # add new item
        self.cache.add(item)
        self.queue.append(item)

        return "miss"

def fifo(k, m, r):
    cache = FIFO(k)
    misses = 0

    for i in range(m):
        if cache.request(r[i]) == "miss":
            misses += 1
    
    return misses