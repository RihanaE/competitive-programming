class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1=m -1
        n2=n - 1
        l=m + n - 1
        
        while l >= 0:
            if n2 >=0 and nums2[n2] >= nums1[n1]:
                nums1[l] = nums2[n2]
                l -=1
                n2 -=1
                
            elif n1 < 0:
                nums1[l] = nums2[n2]
                l -=1
                n2 -=1

            else:
                nums1[l]= nums1[n1]
                l -=1
                n1 -=1
                    