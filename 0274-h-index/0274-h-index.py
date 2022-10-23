class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        for i, value in enumerate(citations):
            if i >= value:
                return i
            
        return len(citations)