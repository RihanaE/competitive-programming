# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)

        temp = root
        parent = None
        
        while temp:
            
            if temp.val < val:
                parent = temp
                temp = temp.right
                
                if not temp:
                    parent.right = TreeNode(val)
                
            else:
                parent = temp
                temp = temp.left
                if not temp:
                    parent.left = TreeNode(val)
                    
                
        
        return root