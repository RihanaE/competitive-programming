class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        store = set()
        for i in nums:
            self.helper(i, store)
        
        return len(store)
        
    def helper(self, num, store):
        d = 2
        while d * d <= num:
            if num % d == 0:
                store.add(d)
                
                while num % d == 0:
                    num = num // d
                    
            d += 1
            
        if num > 1:
            store.add(num)
            
        return store