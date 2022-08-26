class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new = sorted(set(nums), reverse=True)
        if (len(new) >= 3):
            return new[2]
        else:
            return new[0]


        return nums