class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        
        
        collection = []
        portion = [0] * 26
        mx_ = 0
       
        
        for word in words:
            for i in word:
                if portion[ord(i) - 97] == 0:
                    portion[ord(i) - 97] = 1
                    
            collection.append(portion[:])
            
            portion = [0] * 26
            
        
        
        for first in range(len(collection) -1, -1, -1):
            for second in range(first - 1, -1, -1):
                res = [x & y for x, y in zip(collection[first], collection[second])]
                
                if sum(res) == 0:
                    mx_ = max(len(words[first]) * len(words[second]), mx_)
                
                
        return mx_