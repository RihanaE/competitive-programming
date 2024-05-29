class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        size = len(candyType) // 2
        type_ = set(candyType)
        
        if len(type_) >= size:
            return size
        return len(type_)