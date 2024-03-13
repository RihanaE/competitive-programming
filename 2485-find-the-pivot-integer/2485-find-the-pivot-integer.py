class Solution:
    def pivotInteger(self, n: int) -> int:
        pre = [1]
        post = [n]
        
        for i in range(2, n + 1):
            pre.append(pre[-1] + i)
            
        for i in range(n - 1, 0, -1):
            post.append(post[-1] + i)
            
        post = post[::-1]
            
        for i in range(len(pre)):
            if post[i] == pre[i]:
                return i + 1
            
        return -1