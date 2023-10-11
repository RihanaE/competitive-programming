from collections import defaultdict, deque


no_nodes, no_edges = list(map(int, input().split(" ")))
graph = []
cycle = defaultdict(list)

for _ in range(no_edges):
    src, dest, weight = list(map(int, input().split(" ")))
    cycle[src].append([dest, weight])
    graph.append([src, dest, weight])

distance = [float("inf")] * no_nodes

distance[0] = 0
res = None

for i in range(no_nodes - 1):
    for src, dest, weght in graph:
        if distance[src - 1] != float("inf") and distance[src - 1] + weight < distance[dest - 1]:
            distance[dest - 1] = distance[src - 1] + weight

for src, dest, weight in graph:
    if distance[src - 1] != float("inf") and distance[src - 1] + weight < distance[dest - 1]:
        res = dest

if res:
    print("YES")
    ans = [res]

    queue = deque({res})
    visited = set()
  
    while queue:
        node = queue.popleft()
        visited.add(node)

        for child, weight in cycle[node]:
            
            if child == res:
                ans.append(res)
                break
            ans.append(child)
            queue.append(child)

    print(*ans)

else:
    print("NO")
