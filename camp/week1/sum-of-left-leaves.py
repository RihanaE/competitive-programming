# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sm_ = 0
        
        def dfs(node, flag):
            nonlocal sm_
            
            if not node.left and not node.right:
                if flag:
                    sm_ += node.val
                    
                return
            if node.left:
                dfs(node.left, True)
                
            if node.right:
                dfs(node.right, False)
            
        dfs(root, False)
        return sm_