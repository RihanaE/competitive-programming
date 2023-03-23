# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        total = 0
        store = defaultdict(int)
        store[0] += 1
        
        def helper(root, targetSum, store, total):
            nonlocal count
            if not root:
                return 
            
            
            total += root.val
            
            
            if total - targetSum in store:
                count += store[total - targetSum]
            
            store[total] += 1
            
            
            helper(root.left, targetSum, store, total)
            helper(root.right, targetSum, store, total)
            
            store[total] -= 1
            
                
        helper(root, targetSum, store, total)
        
        return count