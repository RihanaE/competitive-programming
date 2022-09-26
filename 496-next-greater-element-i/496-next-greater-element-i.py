class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = []

        for i in nums1:
            index = nums2.index(i)
            max = -1

            for j in range(index, len(nums2)):
                if nums2[j] > i:
                    max = nums2[j]
                    break



            store.append(max)

        return store

        