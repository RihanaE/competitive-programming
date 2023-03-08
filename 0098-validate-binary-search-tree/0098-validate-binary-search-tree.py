# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        stack =[[float('-inf'),root, float('inf')]]
        result = True
        
        while stack:
            lower, value, upper = stack.pop()
            if not value:
                continue
                
            if value.val >= upper or value.val <= lower:
                result = False
                return False
            
            
            stack.append([lower, value.left, value.val])
            stack.append([value.val,value.right,upper])
            
            
        
        return result
        
        
#     def helper(self, root, left = -float("inf"), right = float('inf')):
#         if not root:
#             return True
        
#         if (root.val <= left) or (root.val >= right):
#             return False
        
#         left_val = self.helper(root.left, left, root.val)
#         right_val = self.helper(root.right, root.val, right)
        
#         return left_val and right_val
        
