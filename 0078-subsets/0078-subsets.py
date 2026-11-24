class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def helper(res, pointer):
            if pointer >= len(nums):
                ans.append(res)
                return

            helper(res + [nums[pointer]], pointer + 1)
            helper(res, pointer + 1)

        helper([], 0)
        return ans