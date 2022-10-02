class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        output=[]

        for i in s:
            if i == ")":
                while stack[-1] != "(":
                    output.append(stack.pop())

                stack.pop()

                for j in output:
                    stack.append(j)



                output=[]

            else:
                stack.append(i)

        return "".join(stack)
