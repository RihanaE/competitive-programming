class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first = set()
        second = set()
        ans1 = []
        ans2 = []
        
        for i in nums1:
            first.add(i)
            
        for i in nums2:
            second.add(i)
            
        for i in first:
            if i not in second:
                ans1.append(i)
                
        for i in second:
            if i not in first:
                ans2.append(i)
                
        return [ans1, ans2]