class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []
        mn = float('inf')

        for i in range(len(nums)):
            if not stack:
                if mn > nums[i]:
                    mn = nums[i]
                    stack.append([nums[i], mn])

                else:
                    stack.append([nums[i], mn])

            elif stack[-1][0] > nums[i]:
                if mn > nums[i]:
                    mn = nums[i]
                stack.append([nums[i], mn])


            else:

                while stack and stack[-1][0] <= nums[i]:
                    stack.pop()

                if mn > nums[i]:
                    mn = nums[i]

                stack.append([nums[i], mn])

            if len(stack) > 1 and stack[-2][1] != stack[-2][0] and stack[-2][1] < stack[-1][0]:
                return True

        if len(stack) > 1 and stack[-2][1] != stack[-2][0] and stack[-2][1] < stack[-1][0]:
            return True

        else:
            return False