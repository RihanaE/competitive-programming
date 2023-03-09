class Solution:
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        max_ = float('inf')
        trial = [0] * k 
        self.res = []
        
        def backtrack(trial, counter, n, cookies):
            nonlocal max_
            if counter == n:
                max_ = min(max_, max(trial))
                return
            
            
            for i in range(k):
                trial[i] += cookies[counter]
                if max(trial) < max_:
                    self.res.append(backtrack(trial, counter + 1, n , cookies))
                trial[i] -= cookies[counter]
                
#             ans.append(cookies[counter])
#             first = backtrack(ans, counter + 1, n , sum_, cookies, max_)
            
#             ans.pop()
#             second = backtrack(ans, counter + 1, n, sum_, cookies, max_)
            
                   
        # res = backtrack([], 0, n , sum_, cookies, max_)
        # print(res)
        out = backtrack(trial, 0 , n, cookies)
        return max_