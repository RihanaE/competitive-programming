class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 0
        count = 0
        index = 0
        
        
        while r < len(chars):
            if chars[l] == chars[r]:
                count += 1
                r += 1
                
            elif chars[l] != chars[r]:
                if count == 1:
                    chars[index] = chars[l]
                    index += 1
                    count = 0
                    
                else:
                    chars[index] = chars[l]
                    index += 1
                
                    for i in str(count):
                        chars[index] = i
                        index += 1
                    
                    count = 0
                    
                    
                l = r
                
                
        
        chars[index] = chars[l]
        index += 1
        if count > 1:
            for i in str(count):
                chars[index] = i
                index += 1
    
           
            
        return index