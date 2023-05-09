class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        temp = Counter(words)
        store = []
        print(temp)
        for string in temp:
            store.append([temp[string], 0, string])
           
        store.sort()
        for i in range(1, len(store)):
            if store[i][0] == store[i - 1][0]:
                store[i][1] = store[i - 1][1] - 1
            
        heapify(store)
        

        res = nlargest(k, store)
        ans = []
        
        for i in res:
            ans.append(i[2])

            
        return ans