class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_ = []
        end_ = []
        res = []
        
        
        for ind, val in enumerate(intervals):
            start_.append([val[0], ind])
            end_.append(val[1])
            
        start_.sort()
        n = len(end_)
        
        for i in end_:
            res.append(self.helper(i, start_, n))
            
        return res
        
    def helper(self, target, start, end_):
        
        left = 0
        right = end_ - 1
        store = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if start[mid][0] == target:
                return start[mid][1]
            
            elif start[mid][0] < target:
                left = mid + 1
                
            else:
                store = mid
                right = mid - 1
                
        if start[store][0] < target:
            return -1
        
        else:
            return start[store][1]