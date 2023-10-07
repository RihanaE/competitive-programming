class TrieNode():
    def __init__(self):
        self.children = {}
        self.index = -1
        
        
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, idx):
        current = self.root
        
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
                
            current = current.children[i]
            current.index = idx
            
#         current = self.root
#         reverse = word[::-1]
#         pointer = 0
#         j = 0
        
#         while j < len(reverse):
#             if j == pointer:
               
#                 if "#" not in current.children:
#                     current.children["#"] = TrieNode()
                    
#                 current = current.children["#"]
#                 current.index = idx
                
#                 for i in word:
#                     if i not in current.children:
#                         current.children[i] = TrieNode()

#                     current = current.children[i]
#                     current.index = idx
                    
#                 current = self.root
#                 pointer += 1
#                 j = 0
                
                    
#             else:
#                 if reverse[j] not in current.children:
#                     current.children[reverse[j]] = TrieNode()
                    
#                 current = current.children[reverse[j]]
#                 current.index = idx
                
#                 j += 1
                
    def helper(self, word, idx):
        reverse = word[::-1]
        # self.insert("#" + word, idx)
        # self.insert(reverse + "#", idx)
        
        for i in range(len(reverse) + 1):
            self.insert(reverse[:i] + "#" + word, idx)
        
    def search(self, word):
        current = self.root
        
        for i in word:
            if i in current.children:
                current = current.children[i]
                
            else:
                return -1
            
        return current.index
                
class WordFilter:

    def __init__(self, words: List[str]):
        self.collection = Trie()
        
        for idx, word in enumerate(words):
            self.collection.helper(word, idx)
        

    def f(self, pref: str, suff: str) -> int:
        word = suff[::-1] + "#" + pref
        
        return self.collection.search(word)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)