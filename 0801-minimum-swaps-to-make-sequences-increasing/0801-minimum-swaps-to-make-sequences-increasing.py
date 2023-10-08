class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        swap = [float("inf")] * len(nums1)
        unswapped = [float("inf")] * len(nums1)
        swap[0] = 1
        unswapped[0] = 0
        
        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                unswapped[i] = unswapped[i - 1]
                swap[i] = swap[i - 1] + 1
                
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                swap[i] = min(swap[i], unswapped[i - 1] + 1)
                unswapped[i] = min(swap[i - 1], unswapped[i])
                
        return min(swap[len(nums1) - 1], unswapped[len(nums1) - 1])