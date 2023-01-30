class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left_pointer = 0
        right_pointer = len(people) - 1
        count = 0
        
        while left_pointer <= right_pointer:
            if people[right_pointer] + people[left_pointer] <= limit:
                count += 1
                right_pointer -= 1
                left_pointer += 1
                
            else:
                count += 1
                right_pointer -= 1
                
        return count
    
