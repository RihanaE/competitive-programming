# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
  
        
        def helper(node, flag):
            if not node:
                return
            
            elif node.val in to_delete:
                helper(node.left, True)
                helper(node.right, True)
                  
                node = None
                
            else:
                if node.left:
                    if node.left.val in to_delete:
                        helper(node.left, True)
                        node.left = None
                        
                    else:
                        helper(node.left, False)
                        
                if node.right:
                    if node.right.val in to_delete:
                        helper(node.right, True)
                        node.right = None
                        
                    else:
                        helper(node.right, False)
                        
                    
                if flag:
                    res.append(node)
                    
        helper(root, True)
        return res