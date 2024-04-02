# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        
        def helper(node, isRoot):
            if not node:
                
                return 
            
            if node.val in to_delete:
                if node.left:
                    helper(node.left, True)
                    
                if node.right:
                    helper(node.right, True)
                    
                node.val = None
                
                
            else:
                if node.left and node.left.val in to_delete:
                    helper(node.left, True)
                    node.left = None
                    
                elif node.left:
                    helper(node.left, False)
                    
                if node.right and node.right.val in to_delete:
                    helper(node.right, True)
                    node.right = None
                    
                elif node.right:
                    helper(node.right, False)
                   
                
                if isRoot:
                    res.append(node)
                    
        helper(root, True)
        return res