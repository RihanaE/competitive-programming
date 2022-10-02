class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[0]*len(temperatures)


        for i, j in enumerate(temperatures):
            while stack !=[] and stack[-1][0] < j:
                temp, index= stack.pop()
                output[index]= i - index

            stack.append([j , i])

        return output