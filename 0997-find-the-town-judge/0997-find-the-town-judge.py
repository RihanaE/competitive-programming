class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = set()
        graph = defaultdict(list)
        
        for a, b in trust:
            arr.add(a)
            graph[b].append(a)
            
        for i in range(1, n + 1):
            if i not in arr and len(graph[i]) == n - 1:
                return i
            
        return -1