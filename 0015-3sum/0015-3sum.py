class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0

        while i < len(nums):
            if nums[i] not in nums[:i]:
                n1 = nums[i]

                n2 = i + 1
                n3 = len(nums) - 1

                while n3 > n2:
                    if i != n2 != n3 and n1 + nums[n2] + nums[n3] == 0:
                        res.append([n1, nums[n2], nums[n3]])
                        
                        n2 += 1
                        while nums[n2] == nums[n2 - 1] and n2 < n3:
                            n2 +=1
                            
                    elif n1 + nums[n2] + nums[n3] < 0:
                        n2 += 1

                    elif n1 + nums[n2] + nums[n3] > 0:
                        n3 -= 1

                i += 1

            else:
                i += 1

        return res