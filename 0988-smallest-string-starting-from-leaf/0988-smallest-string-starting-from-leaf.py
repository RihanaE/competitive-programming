# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node, ls):
            if not node:
                return
            
            if not node.left and not node.right:
                res.append("".join([chr(node.val + 97)] + ls[:]))
                return
            
            dfs(node.right, [chr(node.val + 97)] + ls)
            dfs(node.left, [chr(node.val + 97)] + ls)
            
        dfs(root, [])
        res.sort()
        return res[0]