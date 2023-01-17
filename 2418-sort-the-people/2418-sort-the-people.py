class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            num = heights[i]
            key = i
             
            for j in range(i + 1, len(names)):
                if heights[j] > num:
                    num = heights[j]
                    key = j
                    
            names[i], names[key] = names[key] , names[i]
            heights[i], heights[key] = heights[key] ,heights[i]
            
            
        return names
            
                    
            