# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q=deque([[0,root]])
        res=0
        while q:
            res=max(res,(q[-1][0]-q[0][0])+1)
            for i in range(len(q)):
                idx,node=q.pop()
                if node.right:
                    q.appendleft([2*idx+1,node.right])
                if node.left:
                    q.appendleft([2*idx,node.left])
        return res
        