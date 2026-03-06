class OPTFF:
    def __init__(self, k, r):
        self.capacity = k
        self.cache = set()
        self.r = r 

    def request(self, i):
        item = self.r[i]

        # hit
        if item in self.cache:
            return "hit"

        # miss
        if len(self.cache) < self.capacity:
            self.cache.add(item)
            return "miss"

        # cache full → choose victim farthest in future
        farthest = -1
        victim = None

        for c in self.cache:
            try:
                next_use = self.r.index(c, i + 1)
            except ValueError:
                # never used again → best victim
                victim = c
                break

            if next_use > farthest:
                farthest = next_use
                victim = c

        self.cache.remove(victim)
        self.cache.add(item)

        return "miss"


def optff(k, m, r):
    cache = OPTFF(k, r)
    misses = 0

    for i in range(m):
        if cache.request(i) == "miss":
            misses += 1

    return misses
