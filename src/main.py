import sys
from fifo import fifo
from lru import lru
from optff import optff


def main():

    with open(sys.argv[1]) as f:

        k, m = map(int, f.readline().split())
        r = list(map(int, f.readline().split()))

    fifo_miss = fifo(k, m, r)
    lru_miss = lru(k, m, r)
    optff_miss = optff(k, m, r)

    print("FIFO  :", fifo_miss)
    print("LRU   :", lru_miss)
    print("OPTFF :", optff_miss)


if __name__ == "__main__":
    main()
