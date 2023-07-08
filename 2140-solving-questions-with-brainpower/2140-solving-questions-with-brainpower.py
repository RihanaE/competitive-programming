class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        pointer = len(questions) - 1
        
        for q in questions[::-1]:
            if q[1] + 1 + pointer < len(questions) :
                dp[pointer] = max(dp[pointer + 1], q[0] + dp[q[1] + pointer + 1])
                
            elif pointer + 1 < len(questions):
                dp[pointer] = max(q[0], dp[pointer + 1])
                
            else:
                dp[pointer] = q[0]
                
            pointer -= 1
            
        return dp[0]