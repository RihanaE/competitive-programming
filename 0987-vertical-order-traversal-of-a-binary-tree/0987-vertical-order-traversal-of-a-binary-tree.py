# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dic = defaultdict(list)
        
        def dfs (root, x = 0, y =0):
            if not root:
                return []
            
            left = dfs(root.left,x + 1, y - 1 )
            curr = [[root.val, x, y]]
            right = dfs(root.right, x + 1 , y + 1)
            
            return left + curr + right
        
        arr = dfs(root)
        arr.sort(key = lambda k :k[2])
        res = []
        
        for val, x, y in arr:
            my_dic[y] += [[x, val]]
        
         
        
        temp1 = []
        for temp in my_dic.values():
            temp.sort()
            temp1.append(temp)
                
        print(temp1)

        for i in temp1:
            arr1 = []
            
            for j in range(len(i)):
                arr1.append(i[j][1])
                
                
            res.append(arr1)
            
    
            
        return res