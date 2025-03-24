class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        interval = 0
        mn = float("inf")
        mx = -float("inf")

        for i in range(len(meetings)):
            if i == 0:
                interval += meetings[0][1] - meetings[0][0] + 1
                mn = meetings[0][0]
                mx = meetings[0][1]

            else:
                if meetings[i][0] <= mx and meetings[i][1] > mx:
                    interval += meetings[i][1] - mx
                    mx = meetings[i][1]

                elif meetings[i][0] <= mx and meetings[i][1] <= mx:
                    continue

                else:
                    interval += meetings[i][1] - meetings[i][0] + 1
                    mx = meetings[i][1]
                # [1, 4], [2, 5], [3, 4]
        
        return days - interval