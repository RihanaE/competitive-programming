# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([root])
        if not root:
            return []
        res=[]
        while q:
            nodes=[]
            temp=[]
            while q:
                curr=q.pop()
                nodes.append(curr)
                temp.append(curr.val)
            res.append(temp)   
            for node in nodes:
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                
            
            
        return res
                
        