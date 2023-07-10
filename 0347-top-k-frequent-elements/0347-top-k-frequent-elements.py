class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count=Counter(nums)
        result=[]
        
        s=sorted(count, key=count.get, reverse=True)
        
        for i in range(k):
            result.append(s[i])
            
        return result   