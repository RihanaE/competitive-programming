class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters = Counter("".join(words))
        size = len(words)
        for letter in letters.values():
            if letter % size != 0:
                return False

            
        return True