# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return
        
        dummy = TreeNode(preorder[0])
        limit = len(preorder)
        
        for i in range(1, len(preorder)):
            if preorder[0] < preorder[i]:
                limit = i
                break
                
        dummy.left = self.bstFromPreorder(preorder[1 : limit])
        dummy.right = self.bstFromPreorder(preorder[limit:])
        
        return dummy
#         curr = dummy
        
#         def helper(curr, pointer):
#             if pointer >= len(preorder):
#                 return
            
#             if preorder[pointer] > curr.val:
#                 return
            
#             curr.left = TreeNode(preorder[pointer])
#             pointer += 1
            
#             helper(curr.left, pointer)
            
            
            
#             if pointer < len(preorder):
#                 curr.right = TreeNode(preorder[pointer])
            
#             pointer += 1
#             helper(curr.right, pointer)    
            
#         helper(curr, 1)
#         return dummy