class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        fleet=[]
        
        for i in range(len(position)):
            fleet.append([position[i], (target - position[i]) / speed[i]])
            
        fleet.sort(key=lambda k:k[0], reverse=True)
        
        for i in fleet:
            if stack == []:
                stack.append(i)
                
            elif stack[-1][1] >= i[1]:
                pass
            else:
                stack.append(i)
                
        return len(stack)