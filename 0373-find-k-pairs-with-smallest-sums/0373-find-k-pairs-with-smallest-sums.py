class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set({(0, 0)})
        heap = []
        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        res = []
        
        while k != 0 and heap:
            sm_, idx1, idx2 = heappop(heap)   
            res.append([nums1[idx1], nums2[idx2]])
            k -= 1
                
            if (idx1 + 1, idx2) not in visited and idx1 + 1 < len(nums1):
                heappush(heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
                visited.add((idx1 + 1, idx2))
                
                
            if (idx1, idx2 + 1) not in visited and idx2 + 1 < len(nums2):
                heappush(heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
                visited.add((idx1, idx2 + 1))
                
                
        return res
    