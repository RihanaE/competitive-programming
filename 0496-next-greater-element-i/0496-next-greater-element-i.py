class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        res = []
        stack = []
        
        for i in nums2:
            if not stack or stack[-1] > i:
                stack.append(i)
                
            elif stack[-1] < i:
                while stack and stack[-1] < i:
                    store[stack.pop()] = i
                    
                stack.append(i)
                
        for i in nums1:
            if i in store:
                res.append(store[i])
                
            else:
                res.append(-1)
            
        return res