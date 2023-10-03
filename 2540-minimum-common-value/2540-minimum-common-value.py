class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        leftPointer = 0
        rightPointer = 0
        
        while leftPointer < len(nums1) and rightPointer < len(nums2):
            if nums1[leftPointer] == nums2[rightPointer]:
                return nums1[leftPointer]
            
            elif nums1[leftPointer] > nums2[rightPointer]:
                rightPointer += 1
                
            else:
                leftPointer += 1
                
        return -1