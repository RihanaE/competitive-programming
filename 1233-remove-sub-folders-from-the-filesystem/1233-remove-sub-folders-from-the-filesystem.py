class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        flag = False
        
        for i in word:
            if i == "/":
                if curr.end:
                    flag = True
                    break
                    
                else:
                    if i not in curr.children:
                        curr.children[i] = TrieNode()
                        
                    curr = curr.children[i]
                    
            else:
                if i not in curr.children:
                    curr.children[i] = TrieNode()
                    
                curr = curr.children[i]
                
        if not flag:
            curr.end = True
            
    def search(self):
        curr = self.root
        res = []
        
        def dfs(node, lst):
            if node.end:
                temp = "".join(lst)
                res.append(temp)
                
            for child in node.children:
                dfs(node.children[child], lst + [child])
           
        dfs(curr, [])
        return res
        
        
                
#         curr = self.root
#         part = []
        
#         for i in word:
#             if i != "/":
#                 part.append(i)
                
#             else:
#                 temp = "".join(part)
                
#                 if temp not in curr.children:
#                     curr.children[temp] = TrieNode()
                    
#                 curr = curr.children[temp]
#                 part = []
                
#         if not part:
#             temp = "".join(part)
                
#             if temp not in curr.children:
#                 curr.children[temp] = TrieNode()

#             curr = curr.children[temp]
            
#         curr.end = True
        
#     def search(self):
#         res = []
#         curr = self.root
        
#         for i in curr.children.keys():
#             res.append(i)
            
#         return res
        
            
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        collection = Trie()
        folder.sort()
        for i in folder:
            collection.insert(i)
            
        return collection.search()
        