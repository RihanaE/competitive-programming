class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        count = Counter(nums)


        for i in (nums):
            if i == k - i and count[i] >= 2:
                count[i] -=2
                output +=1


            elif i != k - i and count[i] > 0 and count[k - i] >0:
                count[i] -= 1
                count[k - i] -= 1
                output += 1



        return output
