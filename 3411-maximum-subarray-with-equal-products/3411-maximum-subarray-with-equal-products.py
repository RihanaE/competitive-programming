class Solution:
    def maxLength(self, nums: List[int]) -> int:
        left = 0
        right = 0
        res = 0
        prod = nums[0]

        def GCD(left, right):
            mn = min(nums[left : right + 1])
            r = 1
            for j in range(mn, 1, -1):
                flag = True
                for i in range(left, right + 1):
                    if nums[i] % j != 0:
                        flag = False
                        break

                if flag:
                    r = j
                    break

            return r

        def LCM(left, right):
            mx = 1
            res = 1
            for i in range(left, right + 1):
                mx *=nums[i]
                res *=nums[i]
                
            for i in range(1, mx):
                flag = True
                for j in range(left, right + 1):
                   
                    if i % nums[j] != 0:
                        flag = False
                        break
                
                if flag:
                    res = i
                    break
            return res

        while right < len(nums):
            gcd = GCD(left, right)
            lcm = LCM(left, right)
         
            
            if  gcd * lcm == prod:
                res = max(res, (right - left) + 1)
                right += 1
               
                if right < len(nums):
                    prod = prod * nums[right]

            elif gcd * lcm < prod:
                prod = prod // nums[left]
                left += 1
                right += 1
                if right < len(nums):
                    prod = prod * nums[right]

            else:
                right += 1
                if right < len(nums):
                    prod = prod * nums[right]
           

        return res