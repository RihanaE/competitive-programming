class TrieNode:
    def __init__(self, amount):
        self.children = {}
        self.isEnd = False
        self.amount = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode(0)
        self.words = defaultdict(int)
        
    def insert(self, word, value):
        current = self.root
        
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode(value)
                
            current = current.children[i]
            current.amount += (value - self.words[word])
            
        current.isEnd = True
        self.words[word] = value
        
    def search(self, prefix):
        current = self.root
        
        for i in prefix:
            if i not in current.children:
                return 0
            
            current = current.children[i]
            
        return current.amount
        
            
class MapSum:

    def __init__(self):
        self.collection = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.collection.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.collection.search(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)