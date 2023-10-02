class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
                
            current = current.children[i]
            
        current.end = True
        
    def search(self, word):
        current = self.root
        return self.dfs(0, current, word)
            
    def dfs(self, pointer, root, word):
        current = root
        
        for i in range(pointer, len(word)):
            if word[i] == ".":
                for child in current.children:
                    if self.dfs(i + 1, current.children[child], word):
                        return True
                    
                return False
                    
            elif word[i] not in current.children:
                return False
            
            else:
                current = current.children[word[i]]
                
        return current.end
    
class WordDictionary:

    def __init__(self):
        self.collection = Trie()

    def addWord(self, word: str) -> None:
        self.collection.insert(word)

    def search(self, word: str) -> bool:
        return self.collection.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)