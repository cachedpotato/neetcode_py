class PrefixTreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = PrefixTreeNode()
            
            curr = curr.children[idx]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        
        return True

def main():
    prefixTree = PrefixTree()
    prefixTree.insert("dog")
    print(prefixTree.search("dog"))
    prefixTree.search("do")
    print(prefixTree.startsWith("do"))
    #prefixTree.insert("do")
    #prefixTree.search("do")

if __name__ == "__main__":
    main()