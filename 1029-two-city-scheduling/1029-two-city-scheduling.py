class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        store = []
        res = 0
        
        for costA, costB in costs:
            store.append([costA, costB, costB - costA])
            
        store.sort(key = lambda k: k[2])
        
        leftPointer = 0
        rightPointer = len(store) - 1
        
        while leftPointer < rightPointer:
            res += (store[leftPointer][1] + store[rightPointer][0])
            leftPointer += 1
            rightPointer -= 1
            
        return res