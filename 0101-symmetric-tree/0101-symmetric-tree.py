# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        temp = root.left
        temp1 = root.right
        
        return self.helper(temp, temp1)
        
            
            
    def helper(self, temp, temp1):
        if (not temp and temp1) or (not temp1 and temp):
            return False
        
        elif not temp and not temp1:
            return True
        
        else:
            if temp.val != temp1.val:
                return False
            
            return self.helper(temp.left, temp1.right) and self.helper(temp.right, temp1.left)