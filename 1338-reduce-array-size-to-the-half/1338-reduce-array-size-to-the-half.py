class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        l=set(arr)
        l=list(l)
        index=len(l)
        total=0
        l.sort(key=lambda k:count[k])
        h=1
        output=[]
        no=len(arr) // 2
        i=0

        while i < len(l) and h < len(l) + 1:
            if count[l[index - h]] > no :
                output.append(l[index - h])
                return len(output)

            elif total < no :
                total += count[l[index - h]]
                output.append(l[index - h])
                h+=1
                i +=1

            if total >= no :
                return len(output)

        