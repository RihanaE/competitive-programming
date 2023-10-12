# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        
        def dfs(node):
            nonlocal moves
            
            if node is None:
                return 0
            
            currentsm = node.val - 1
            
            right = dfs(node.right)
            left = dfs(node.left)
    
            currentsm += left + right
            moves += abs(currentsm)
            return currentsm
            
        dfs(root)
        
        return moves