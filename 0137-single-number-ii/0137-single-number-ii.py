class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        B = [0] * 32
        for x in nums:
            x+=(1<<31)
            for i in range(32):
                if x & (1 << i):
                    B[i] += 1
        ans = 0
        for i in range(32):
            if B[i] % 3 != 0:
                ans |= (1 << i)
        return ans-(1<<31)