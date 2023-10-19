class TrieNode:
    def __init__(self):
        self.children = {}
        self.sm = 0
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
                
            curr = curr.children[i]
            curr.sm += 1
            
        curr.end = True
        
    def search(self, word):
        res = 0
        curr = self.root
        
        for i in word:
            curr = curr.children[i]
            res += curr.sm
            
        return res
            
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        collection = Trie()
        res = []
        
        for word in words:
            collection.insert(word)
            
        for word in words:
            res.append(collection.search(word))
            
        return res