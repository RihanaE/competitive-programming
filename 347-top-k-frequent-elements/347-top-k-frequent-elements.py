class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        output=[]

        for i in nums:
            if i in store:
                store[i] += 1

            else:
                store[i] = 1

        temp=[]
        for i in list(store):
            value=store[i]
            temp.append(value)

        temp.sort()

        temp2=[]
        h=0
        for i in range(k):
            temp2.append(temp[-1 - h])
            h+=1


        for j, s  in store.items():

            if s in temp2:
                output.append(j)
                temp2.remove(s)

        return output
        