class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pointer1 = 0
        pointer2 = 0
        
        while len(nums1) > pointer1 and len(nums2) > pointer2:
            if nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
                
            elif nums1[pointer1] > nums2[pointer2]:
                pointer2 += 1
                
            else:
                return nums1[pointer1]
            
        return -1