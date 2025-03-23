class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for src, dest, t in roads:
            graph[src].append([dest, t])
            graph[dest].append([src, t])

        minHeap = [(0, 0 )]
        minCost = [float("inf")] * n
        path = [0] * n
        path[0] = 1

        while minHeap:
            cost, node = heappop(minHeap)

            for child, childCost in graph[node]:
                if cost + childCost < minCost[child]:
                    minCost[child] = cost + childCost
                    path[child] = path[node]
                    heappush(minHeap, (cost + childCost, child))

                elif cost + childCost == minCost[child]:
                    path[child] = (path[child] + path[node]) % (10 ** 9 + 7)

        return path[n - 1]