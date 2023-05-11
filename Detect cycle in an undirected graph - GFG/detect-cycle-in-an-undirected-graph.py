from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		graph = defaultdict(list)
		
		for i in range(V):
		    graph[i].extend(adj[i])
		    
		visited = set()
		queue = deque()
		
		for i in range(V):
		    if i not in visited:
		        queue.append((i, None))
		        visited.add(i)
		        
		        while queue:
		            node, parent = queue.popleft()
		            
		            for neigh in graph[node]:
		                if neigh in visited and neigh != parent:
		                    return 1
		                    
		                elif neigh in visited and neigh == parent:
		                    continue
		                
		                elif neigh not in visited:
		                    queue.append((neigh, node))
		                    visited.add(neigh)
		                    
        return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends