# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = Counter(self.get_nodes(root))
        out = []
        arr = []
        
        for i, j in res.items():
            out.append([i, j])
            
        out.sort(key = lambda k : k[1])
        arr.append(out[-1][0])
        temp = out[-1][1]
        
        for i in range(len(out) - 2, -1, -1):
            if temp == out[i][1]:
                arr.append(out[i][0])
                
                
        return arr
        
    def get_nodes(self, root):
        if not root:
            return []
        
        else:
            left = self.get_nodes(root.left)
            right = self.get_nodes(root.right)
            curr = [root.val]
            
            return left + curr + right