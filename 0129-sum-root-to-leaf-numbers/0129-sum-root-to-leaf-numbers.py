# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      
        def dfs(root, temp):
            
            if not root:
                return 0
            
            temp = (temp * 10) + root.val
            
            if not root.left and not root.right:
                return temp
            
            return dfs(root.left, temp) + dfs(root.right, temp)
            
        return dfs(root, 0)
       