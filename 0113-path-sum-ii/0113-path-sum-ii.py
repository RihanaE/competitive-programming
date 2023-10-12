# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        if not root:
            return []
                    
        def dfs(node, lst, sm_):
            if (not node.left) and (not node.right):
           
                if sm_ + node.val == targetSum:
                    temp = lst + [node.val]
                    res.append(temp[:])
                    
                return
                    
            if node.left:
                dfs(node.left, lst + [node.val], sm_ + node.val)
                
            if node.right:
                dfs(node.right, lst + [node.val], sm_ + node.val)
            
        dfs(root, [], 0)
        return res