class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        flag = False
        
        for j in range(len(names)):
            for i in range(len(names) - 2 , -1,-1):
                if heights[i + 1] > heights[i]:
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]
                    names[i], names[i + 1] = names[i + 1], names[i]
                    flag = True
                    
            if flag == False:
                break
                
        return names