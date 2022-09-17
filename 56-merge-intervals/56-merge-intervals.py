class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        store=[intervals[0]]
        
        for first , last in intervals[1:]:

            end= store[-1][1]
            if first <= end:
                store[-1][1]=max(last, end)

            else:
                store.append([first,last])

        return store