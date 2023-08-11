class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)

      
        adj_list = {i: [] for i in range(n)}
        for i in range(1, n):
            adj_list[parent[i]].append(i)

       
        def dfs(node):
            max_value = max_leg1 = max_leg2 = 0
            for child in adj_list[node]:
               
                (leg, value) = dfs(child)
                if s[child] == s[node]:
                    leg = 0

               
                if leg > max_leg1:
                    max_leg2, max_leg1 = max_leg1, leg
                elif leg > max_leg2:
                    max_leg2 = leg

               
                max_value = max(value, max_value)

         
            max_value = max(max_value, (max_leg1 + max_leg2 + 1))
            return (max_leg1 + 1, max_value)

        _, max_value = dfs(0)
        return max_value