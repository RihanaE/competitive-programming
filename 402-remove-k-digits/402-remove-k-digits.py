class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            if stack == []:
                stack.append(i)

            elif int(stack[-1]) > int(i):
                while stack and int(stack[-1]) > int(i) and k != 0:
                    stack.pop()
                    k -=1
                stack.append(i)

            else:
                stack.append(i)
                
        while stack and k != 0:
            stack.pop()
            k -=1
            
        if len(stack) == 0:
            stack.append("0")



        return str(int("".join(stack)))

        