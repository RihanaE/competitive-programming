# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sm = 0
        
        stack = [[None, None, root]]
        
        while stack:
            grand, child, root = stack.pop()
            
            if grand and grand.val % 2 == 0:
                sm += root.val
                
            if root.right:
                stack.append([child, root, root.right])
                
            if root.left:
                stack.append([child, root, root.left])            
                
        return sm