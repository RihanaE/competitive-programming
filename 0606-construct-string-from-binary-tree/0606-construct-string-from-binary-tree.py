# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            if not root:
                return ""

            cur = root.val
            left = root.left
            right = root.right
            
            if not right and not left:
                return str(cur)
            
            elif not right:
                return str(cur) + "(" + dfs(left) + ")"
                
            else:
                return str(cur) + "(" + dfs(left) + ")" +  "(" + dfs(right) + ")"
        
        return dfs(root)