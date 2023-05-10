class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for i in piles:
            heap.append(-1 * i)
            
        heapify(heap)
        
        for i in range(k):
            value = heappop(heap)
            value = value * -1
            temp = floor(value / 2)
            value = value - temp
            heappush(heap, value * -1)
            
        return sum(heap) * -1