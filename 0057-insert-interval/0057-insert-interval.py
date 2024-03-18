class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        merged.append(newInterval)
        
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
#         newArr = []
#         pointer = 0
#         store = set()
#         for i in range(len(intervals)):
#             store.add(i)
#         for i in range(len(intervals)):
#             if (intervals[i][0] <= newInterval[0] <= intervals[i][1]) or (intervals[i][0] <= newInterval[1] <= intervals[i][1]):
#                 newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
#                 store.remove(i)
                
#         while pointer < len(intervals):
#             if pointer in store:
#                 if newInterval[1] < intervals[i][0]:
#                     newArr.append(newInterval)

#                 else:
#                     newArr.append(intervals[i])
                    
#             pointer += 1
            
#         print(store)
            
                
#         return newArr