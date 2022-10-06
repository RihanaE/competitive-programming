class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q=deque()
        q.append([0,0])
        sum=0
        output=float('inf')

        for i, n in enumerate(nums):
            sum+=n

            while q and sum - q[0][1] >= k:    
                output=min(output, i - q[0][0] + 1)
                q.popleft()

            while q and sum <= q[-1][1]:
                q.pop()

            q.append([i + 1,sum])


        if output < float('inf'):
            return output
        else:
            return -1