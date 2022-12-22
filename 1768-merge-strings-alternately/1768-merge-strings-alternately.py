class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn=0
        w1_pointer=0
        w2_pointer=0
        s=""
        
        while w1_pointer < len(word1) and w2_pointer < len(word2):
            if turn % 2 == 0:
                s +=word1[w1_pointer]
                w1_pointer +=1
                turn +=1
                
            else:
                s +=word2[w2_pointer]
                w2_pointer +=1
                turn +=1
                
        if w1_pointer < len(word1):
            s +=word1[w1_pointer:]
            
        elif w2_pointer < len(word2):
            s +=word2[w2_pointer:]
            
        return s