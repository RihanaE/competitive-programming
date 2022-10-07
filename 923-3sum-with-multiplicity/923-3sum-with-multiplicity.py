class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        count=Counter(arr)
        keys=sorted(count)
        res=0

        for i, n1 in enumerate(keys):
            j=i
            k=len(keys) - 1
            t=target - n1


            while j <= k:
                n2=keys[j]
                n3=keys[k]
                if n2 + n3 < t:
                    j +=1

                elif n2 + n3 > t:
                    k -=1

                else:
                    if i < j < k:
                        res+=count[n1] * count[n2] * count[n3]

                    elif i == j < k:
                        res+=count[n1] * ((count[n2] - 1)/2) * count[n3]

                    elif i < j == k:
                        res+=count[n1] * count[n2] * ((count[n3] - 1) / 2)

                    else :
                        res+=count[n1] * ((count[n2] - 1)) * ((count[n3] - 2)/6)

                    j +=1
                    k -=1



        return int(res % mod)
