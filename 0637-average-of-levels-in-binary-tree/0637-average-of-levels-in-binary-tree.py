# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque([root])
        
        while queue:
            value = []
            sm = 0
            while queue:
                temp = queue.popleft()
                value.append(temp)
                sm += temp.val
                
            res.append(sm/len(value))
            
            for i in value:
                if i.left:
                    queue.append(i.left)
                    
                if i.right:
                    queue.append(i.right)
                    
        return res