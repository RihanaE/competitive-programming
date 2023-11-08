class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        amount = Counter(arr)
        num = list(amount.values())
        
        return len(num) == len(set(num))