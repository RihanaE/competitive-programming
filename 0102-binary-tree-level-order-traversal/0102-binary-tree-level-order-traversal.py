# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        visited = set()
        res = []
        
        while queue:
            nodes = []
            values = []
            
            while queue:
                val = queue.popleft()
                nodes.append(val)
                values.append(val.val)
                
            res.append(values)
            
            for i in nodes:
                if i.left:
                    queue.append(i.left)
                    
                if i.right:
                    queue.append(i.right)
                    
        return res