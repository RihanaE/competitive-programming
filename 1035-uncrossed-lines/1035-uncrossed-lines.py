class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        collection = {}
        
        def dfs(idx1, idx2):
            if idx1 == len(nums1) or idx2 == len(nums2):
                return 0
            
            if (idx1, idx2) in collection:
                return collection[(idx1, idx2)]
            
            elif nums1[idx1] == nums2[idx2]:
                collection[(idx1, idx2)]= 1 + dfs(idx1 + 1, idx2 + 1)
                return collection[(idx1, idx2)]
            else:
                collection[(idx1, idx2)] = max(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))
                return collection[(idx1, idx2)]
                
        return dfs(0, 0)