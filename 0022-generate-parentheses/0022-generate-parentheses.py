class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        
        def backtracking(o,c):
            if o == c ==n:
                res.append("".join(stack))
                return 
            
            if o < n:
                stack.append("(")
                backtracking(o + 1,c)
                stack.pop()
                
            if c < o:
                stack.append(")")
                backtracking(o,c + 1)
                stack.pop()
                
        backtracking(0, 0)
        return res