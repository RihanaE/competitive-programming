# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        coll = defaultdict(list)
        visited = set([target.val])
        if k == 0:
            return [target.val]
       
        
        def bfs():
            queue = deque([[[root, None]]])
            
          
            while queue:
                node = queue.popleft()
                temp = []
                
                while node:
                    value, parent = node.pop()
                
                    
                    if value and parent:
                        coll[value.val].append(parent.val)
                        coll[parent.val].append(value.val)
                        
                        
                    if value:
                        temp.append([value.left,value] )
                        temp.append([value.right, value])
                        
                        
                if temp:
                   
                    queue.append(temp)
                
            
        bfs()
        nodes = [target.val]
        temp = []
        for i in range(k):
            temp = []
            
            while nodes:
                node = nodes.pop()
                
               
                for j in coll[node]:
                    if j not in visited:
                        visited.add(j)
                        temp.append(j)
                        
            nodes.extend(temp)
            
        return temp
