class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
                
            current = current.children[i]
            current.count += 1
            
        current.isEnd = True
        
    def search(self, word):
        res = 0
        current = self.root
        
        for i in word:
            current = current.children[i]
            res += current.count
            
            
        return res
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        collection = Trie()
        for word in words:
            collection.insert(word)
            
        res = []
        
        for word in words:
            res.append(collection.search(word))
            
        return res