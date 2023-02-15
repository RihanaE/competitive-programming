class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        first_pointer = 0
        second_pointer = 0
        count = 0
        
        if players[0] > trainers[-1]:
            return count
        
        while first_pointer < len(players) and second_pointer < len(trainers):
            if players[first_pointer] <= trainers[second_pointer]:
                count += 1
                first_pointer +=1
                second_pointer +=1
                
            else:
                second_pointer += 1
            
            
        return count