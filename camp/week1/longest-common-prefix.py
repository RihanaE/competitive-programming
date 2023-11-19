class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        collection = Trie()
        
        for word in strs:
            collection.insert(word)
        
        return collection.count(collection.root, '')

       
        
        
class TrieNode:
    def __init__(self):
        self.children = {}
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

        current.isEnd = True
        
    def count(self, current, pre):
        
        if len(current.children) != 1:
            return pre
    
        elif current.isEnd:
            return pre
        
        for child in current.children:
            return self.count(current.children[child], pre + child)
        
        
        