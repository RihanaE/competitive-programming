class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        leftPointer = 0
        rightPointer = 0
        nums1.sort()
        nums2.sort()
        
        while leftPointer < len(nums1) and rightPointer < len(nums2):
            if nums1[leftPointer] == nums2[rightPointer]:
                res.append(nums1[leftPointer])
                leftPointer += 1
                rightPointer += 1
                
            elif nums1[leftPointer] > nums2[rightPointer]:
                rightPointer += 1
                
            elif nums1[leftPointer] < nums2[rightPointer]:
                leftPointer += 1
                
        return res