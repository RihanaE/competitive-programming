# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftM = dfs(root.left)
            rightM = dfs(root.right)
            
            leftM  = max(leftM, 0)
            rightM = max(rightM, 0)
            
            ans[-1] = max(ans[-1], root.val + leftM + rightM)
            
            return root.val + max(leftM, rightM)
        
        dfs(root)
        return ans[0]