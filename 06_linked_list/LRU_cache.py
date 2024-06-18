#LRU CACHE
#WE need O(1) lookup time and insertion time - how do we do it?
#O(1) lookup: use hashmaps, but here's the catch:
#instead of storing key: value pairs, store KEY: Node(KEY, VALUE) Pairs
#This way rearrangement of nodes will become a lot easier
#in the LRUCache Class: have left and right nodes, where
#left: LRU pointer, right: MRU pointer
#besides the cache, we will also store the nodes in a DOUBLY LINKED LIST
#why double? with single, we can't get O(1) time for insertion and deletion

class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.used = []
        self.capacity = capacity

        #LRU, MRU pointer initialization
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    #############HELPER FUNCTIONS################
    #remove from DLL
    def remove(self, node:Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    #insert to the MRU side of the DLL
    def insert(self, node: Node) -> None:
        prev = self.right.prev
        #insert node
        prev.next = self.right.prev = node
        #node pointers
        node.prev = prev
        node.next = self.right
    #############################################

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        #the node has been used - UPDATE THE LIST
        self.remove(node)
        self.insert(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        #if already existing key, remove from list first
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #if cache full, remove the LRU node
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)

def main():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 10)
    print(lRUCache.get(1))
    lRUCache.put(2, 20)
    lRUCache.put(3, 30)
    print(lRUCache.get(2))
    print(lRUCache.get(1))

if __name__ == "__main__":
    main()