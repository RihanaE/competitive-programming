class Solution:
    def isHappy(self, n: int) -> bool:
        def squa(arr,d):
            s=0
            
            for i in arr:
                s+=i * i
            
            if s == 1:
                return True
            
            if s in d.keys():
                return False
            elif s not in d.keys():
                d[s]=1
                
            a=str(s)
            arr=[]
            
            for i in a:
                arr.append(int(i))
                
            return squa(arr,d)
        d={} 
        if n == 1:
            return True
        
        else:
            d[n]=1
            a=str(n)
            arr=[]
            
            for i in a:
                arr.append(int(i))
                
            return squa(arr,d)