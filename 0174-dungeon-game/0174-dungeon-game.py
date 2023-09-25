class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def bound(row, col):
            return 0 <= row < len(dungeon) and 0 <= col < len(dungeon[0])
        
        for i in range(len(dungeon[0]) - 1, -1, -1):
            for j in range(len(dungeon) - 1, -1, -1):
                if i == len(dungeon[0]) - 1 and j == len(dungeon) - 1:
                    if dungeon[j][i] >= 0:
                        dungeon[j][i] = [dungeon[j][i], 0]
                        continue
                        
                    else:
                        dungeon[j][i] = [dungeon[j][i], dungeon[j][i]]
                        continue
                    
                    
                temp = dungeon[j][i]
                if bound(j + 1, i + 1):
                    
                    if dungeon[j + 1][i][1] > dungeon[j][i + 1][1]:
                        value = dungeon[j + 1][i][0] + temp
                        
                    else:
                        value = dungeon[j][i + 1][0] + temp
                        
                    if temp > 0 and temp + max(dungeon[j + 1][i][1], dungeon[j][i + 1][1]) >= 0:
                        mn_value = 0
                        
                    else:
                        mn_value =  max(dungeon[j + 1][i][1], dungeon[j][i + 1][1]) + temp
                        
                        
                elif i + 1 < len(dungeon[0]):
                    temp = dungeon[j][i]
                    value = dungeon[j][i] + dungeon[j][i + 1][0]
                    
                    if temp > 0 and temp + dungeon[j][i + 1][1] >= 0:
                        mn_value = 0
                        
                    else:
                        mn_value = dungeon[j][i + 1][1] + temp
                        
                else:
                    temp = dungeon[j][i]
                    value = dungeon[j][i] + dungeon[j + 1][i][0]
                    
                    if temp > 0 and temp + dungeon[j + 1][i][1] >= 0:
                        mn_value = 0
                        
                    else:
                        mn_value = dungeon[j + 1][i][1] + temp
                    
                        
                dungeon[j][i] = [value, mn_value]
                        
        print(dungeon)              
        if dungeon[0][0][1] >= 0:
            return 1
        
        else:
            return (-1 * (dungeon[0][0][1])) + 1