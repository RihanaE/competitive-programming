class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer_first = m - 1
        pointer_second = n - 1
        main = m + n - 1
        
        while pointer_first >= 0 and pointer_second >= 0:
            if nums1[pointer_first] >= nums2[pointer_second]:
                nums1[main] = nums1[pointer_first]
                main -=1
                pointer_first -= 1
                
            else:
                nums1[main] = nums2[pointer_second]
                pointer_second -= 1
                main -= 1
                
        while pointer_second >= 0:
            nums1[main] = nums2[pointer_second]
            main -= 1
            pointer_second -= 1