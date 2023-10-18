class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        length = len(word)
        
        vowel = set({"a", "e", "i", "o", "u"})
        
        for i in range(length):
            if word[i] in vowel:
                count += ((i + 1) * (length - i))
                
        return count