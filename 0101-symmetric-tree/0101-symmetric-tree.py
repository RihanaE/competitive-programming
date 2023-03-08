# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [[root.left, root.right]]
        result = True
        
        while stack:
            r1, r2 = stack.pop()
            
            if not r1 and not r2:
                continue
                
            elif (not r1 and r2) or (not r2 and r1) or (r1.val != r2.val):
                result = False
                continue
                
            else:
                stack.append([r1.left, r2.right])
                stack.append([r1.right, r2.left])
                
        return result