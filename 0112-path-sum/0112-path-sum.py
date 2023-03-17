# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        return self.helper(root, 0, targetSum, False)
        
    def helper(self, root, total, target, flag):
        if not root:
            if total == target and flag == True:
                return True
            
            else:
                return False
        
        
        if not root.left and not root.right:
            flag = True
            
        else:
            flag = False
        return self.helper(root.left, total + root.val, target, flag) or self.helper(root.right, total + root.val, target, flag)