class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def helper(num, count):
            if num == 1.0:
                return count
           
            if num % 2 != 0:
                ans = helper((3 * num) + 1, count + 1)
                
            else:
                ans = helper(num // 2, count + 1)
            return ans
        
        store = []
        
        for i in range(lo, hi + 1):
            store.append([helper(i, 0), i])
            
        store.sort()
      
        return store[k - 1][1]