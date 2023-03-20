# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def helper(root, lst, flag):
            if not root and flag:
                if "->".join(lst[:]) not in res:
                    res.append("->".join(lst[:]))
                return
            
            elif not root:
                return
                
            if not root.left and not root.right:
                flag = True
                
            else:
                flag = False
                
            helper(root.left, lst + [str(root.val)], flag)
            helper(root.right, lst + [str(root.val)], flag)
            
        helper(root, [], False)
        
        return res