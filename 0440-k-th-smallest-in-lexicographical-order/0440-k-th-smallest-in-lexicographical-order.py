# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.end = False
        
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def insert(self, num):
#         current = self.root
        
#         for i in num:
#             if i not in current.children:
#                 current.children[i] = TrieNode()
                
#             current = current.children[i]
            
#         current.end = True
        
#     def search(self, k):
#         current = self.root
        
        
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k > 0:
            steps = self.getSteps(n, cur, cur+1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1

        return cur

    def getSteps(self, n: int, n1: int, n2: int) -> int:
        steps = 0

        while n1 <= n:

            steps += min(n+1, n2) - n1
            n1 *= 10
            n2 *= 10

        return steps