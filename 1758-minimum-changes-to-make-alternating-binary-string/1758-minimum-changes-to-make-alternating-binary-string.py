class Solution:
    def minOperations(self, s: str) -> int:
        ans = []
        for i in range(len(s)):
            if not ans:
                ans.append("1")
                
            else:
                ans.append(str(1 - int(ans[-1])))
        op = 0       
        for _ in range(len(s)):
            if s[_] != ans[_]:
                op += 1
                
        return min(op, len(s) - op)