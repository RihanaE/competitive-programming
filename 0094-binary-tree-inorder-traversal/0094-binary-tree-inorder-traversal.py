# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return 
        
        else:
            temp = self.inorderTraversal(root.left)
            if temp:
                res.extend(temp)
                
            res.append(root.val)
            
            temp = self.inorderTraversal(root.right)
            
            if temp:
                res.extend(temp)
            
            return res