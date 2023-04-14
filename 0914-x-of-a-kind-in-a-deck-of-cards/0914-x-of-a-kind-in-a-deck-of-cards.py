class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
       
        count = Counter(deck)
        mn = min(count.values())
        if mn <= 1:
            return False
        
        val = mn
        for i in count.values():
            val = gcd(i, val)
            
        if val >= 2:
            return True
        
        return False
        
    def gcd(self, a, b):
        if b == 0:
            return a
        
        return self.gcd(b, a % b)
#         store = self.is_div(mn)
        
        
#         for j in store:
#             flag = True
            
#             for i in count.values():
#                 if i % j != 0:
#                     flag = False
#                     break
                    
#             if flag:
                
#                 return True
            
#         return False
    
#     def is_div(self, num):
#         d = 2
#         ls = set([num])
        
#         if num % d == 0:
#             ls.add(d)
#             while num % d == 0:
#                 num = num // d
                
#         d += 1
        
#         return ls