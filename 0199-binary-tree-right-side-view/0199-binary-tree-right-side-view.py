# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        out = []
        
        if not root:
            return []
        
        while q:
            nodes = []
            temp = []
            
            while q:
                value = q.pop()
                nodes.append(value)
                temp.append(value.val)
                
            for node in nodes:
                if node.left:
                    q.appendleft(node.left)
                    
                if node.right:
                    q.appendleft(node.right)
                    
            res.append(temp)
        
        for i in res:
            out.append(i[-1])
            
        return out