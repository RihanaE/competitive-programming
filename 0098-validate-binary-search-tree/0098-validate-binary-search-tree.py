# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.helper(root)
        
        return result
        
        
    def helper(self, root, left = -float("inf"), right = float('inf')):
        if not root:
            return True
        
        if (root.val <= left) or (root.val >= right):
            return False
        
        left_val = self.helper(root.left, left, root.val)
        right_val = self.helper(root.right, root.val, right)
        
        return left_val and right_val
        
#         if root.left:
#             left = max(root.left.val, self.helper(root.left, val, left, right, result)[0])
#             if left > val:
#                 result = False
                
#             if root.val < root.left.val:
#                 result = False
            
        
            
            
#         if root.right:
#             right = min(root.right.val, self.helper(root.right, val, left, right, result)[0])
#             if right < val:
#                 result = False
                
#             if root.right.val < root.val:
#                 result = False
            
#         print(result)
            
        
#         if left:
#             return [left, result]
        
#         return [right, result]
#         # return [left, right, result]