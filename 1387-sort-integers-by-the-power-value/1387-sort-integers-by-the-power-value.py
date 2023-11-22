class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        
        def helper(num, step):
            if num == 1:
                return step
            
            if num % 2 == 0:
                return helper(num // 2, step + 1)
                
            else:
                return helper((3 * num) + 1, step + 1)
                
        for i in range(lo, hi + 1):
            res.append([helper(i, 0), i])
            
        res.sort()
        return res[k - 1][1]
        
        
#         res = []
        
#         def helper(num):
#             step = 0
#             while num != 1:
#                 if num % 2 == 0:
#                     num = num // 2
                    
#                 else:
#                     num = (3 * num) + 1
                    
#                 step += 1
                
#             return step
        
#         for i in range(lo, hi + 1):
#             res.append([helper(i), i])
            
#         res.sort()
#         return res[k - 1][1]