class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
            res = 0

            if tickets[k] == 0:
                return 0

            counter = 0
            while tickets[k] > 0:
                if counter == len(tickets):
                    counter = counter % len(tickets)

                if tickets[counter] != 0:
                    tickets[counter] -= 1
                    res += 1

                counter += 1

            return res