"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        graph = defaultdict(int)

        graph[root] = 1
        visited= set()

        def dfs(graph, root):
       
            
            if root in visited:
                return 

            visited.add(root)
            
            for node in root.children:
                if not node:
                    return 
                    
                if node not in visited:
                    graph[node] = graph[root] + 1
                    dfs(graph, node)

        dfs(graph, root)
        return max(graph.values())