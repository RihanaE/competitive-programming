class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        leftPointer = 0
        rightPointer = 0
        
        while leftPointer < len(nums1) and rightPointer < len(nums2):
            if nums1[leftPointer] == nums2[rightPointer] and nums1[leftPointer] not in res:
                res.append(nums1[leftPointer])
                leftPointer += 1
                rightPointer += 1
                
            elif nums1[leftPointer] == nums2[rightPointer]:
                leftPointer += 1
                rightPointer += 1
                
            elif  nums1[leftPointer] < nums2[rightPointer]:
                leftPointer += 1
                
            elif nums1[leftPointer] > nums2[rightPointer]:
                rightPointer += 1
                
        return res