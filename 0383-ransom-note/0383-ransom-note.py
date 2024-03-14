class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomeCount = Counter(ransomNote)
        magazineCount = Counter(magazine)
        
        for key, val in ransomeCount.items():
            if magazineCount[key] < val:
                return False
            
        return True