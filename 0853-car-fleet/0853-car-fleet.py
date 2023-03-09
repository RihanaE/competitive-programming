class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            rem_speed = (target - position[i]) / speed[i]
            stack.append([position[i] , rem_speed])
            
        res = []
        count = 0
        stack.sort(reverse = True)
        stack1 = []
        
        for i, j in stack:
            if not stack1:
                stack1.append([i, j])
                count += 1
                
            elif stack1[-1][1] >= j:
                continue
                
            else:
                stack1.append([i, j])
                count += 1
                
        return count