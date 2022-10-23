class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
            
        def checker(arr):
            diff=arr[1] - arr[0]
            p =1
            while p < len(arr):
                if arr[p] - arr[p - 1] != diff:
                    return False
                p +=1
                
            else: return True
            
            
            
        lp, rp =0 , 0
        stack=[]
        
        while rp < len(r):
            check=sorted(nums[l[lp] : r[rp] + 1])
            stack.append(checker(check))
            lp +=1
            rp +=1
            
        return stack