class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0] * (len(arr) + 1)
        output=[]
        
        for i in range(len(arr)):
            prefix[i + 1]= prefix[i] ^ arr[i]
            
        for l, r in queries:
            output.append(prefix[l] ^ prefix[r + 1])
            
        return output