class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        stack=[]
        for i in range(1, n + 1):
            stack.append(i)
        
        self.l=0
        
       
            
        def winner(stack,k,l):
            if len(stack) == 1:
                return stack [0]
            else:
                self.l=(self.l + k - 1) % len(stack)
                stack.remove(stack[self.l])
                return winner(stack,k,self.l)
        
        if len(stack) == 1:
            return stack [0]
        else:
            return winner(stack,k,self.l)