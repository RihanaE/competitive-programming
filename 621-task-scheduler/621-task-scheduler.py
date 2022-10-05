class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        max_heap=[]
        for i in count.values():
            max_heap.append(-i)

        heapq.heapify(max_heap)

        t=0
        q=deque()

        while max_heap or q:
            t+=1

            if max_heap!= []:
                i=1 + heapq.heappop(max_heap)
                if i != 0:
                    q.append([i, t + n])

            if q and q[0][1] == t:
                heapq.heappush(max_heap, q.popleft()[0])


        return t

