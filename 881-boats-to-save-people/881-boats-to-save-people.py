class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        output=0
        i=0
        j=len(people) - 1
        people.sort()
        while i <= j:
            if people[i] + people[j] <= limit:
                output+=1
                i+=1
                j-=1

            elif people[j] <= limit:
                output+=1
                j-=1



        return output
        