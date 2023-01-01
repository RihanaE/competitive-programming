class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = 0
        for i in nums:
            if i % 2 == 0:
                result += i

        output = []
        count = 0
        for i in nums:
            temp=nums[queries[count][1]]
            nums[queries[count][1]] = nums[queries[count][1]] + queries[count][0]

            if temp % 2 == 0:
                result -= temp
                if nums[queries[count][1]] % 2 == 0:
                    result += nums[queries[count][1]]

            else:
                if nums[queries[count][1]] % 2 == 0:
                    result += nums[queries[count][1]]

            output.append(result)
            count += 1

        return output