class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p=[]
        stack=[]

        for i in range(len(position)):
            p.append([position[i], speed[i]])

        p.sort(key= lambda k : k[0])

        for i,j in p[::-1]:
            if stack == []:
                stack.append(p.pop())

            elif (target - stack[-1][0]) / stack[-1][1] >= (target - i) / j:
                p.pop()


            else:
                stack.append(p.pop())
        return len(stack)