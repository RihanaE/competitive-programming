class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        store = defaultdict(list)
        res = []
        seen = set([edges[0][0]])
        seen_j = set()
        
        for i, j in edges:
            seen.add(i)
            seen_j.add(j)
            
        for i in seen_j:
            if i in seen:
                seen.remove(i)
           
            
        for i in seen:
            res.append(i)
            
        return res