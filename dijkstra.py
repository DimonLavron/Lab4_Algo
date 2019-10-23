import heapq

with open("dijkstra.in", "r") as f:
    n, s = map(int, f.readline().split())

    maxn = 100005
    inf = float('inf')
    min_path = [inf] * maxn
    n_vertex = -1
    graph = [[] for i in range(maxn)]

    for i in range(n):
        v1, v2, w = map(int, f.readline().split())
        graph[v1].append((v2, w))
        n_vertex = max(n_vertex, max(v1,v2))

    n_vertex += 1
    min_heap = [(0, s)]
    heapq.heapify(min_heap)
    min_path[s] = 0

    while len(min_heap) > 0:
        min_vertex = heapq.heappop(min_heap)[1]

        for v, w in graph[min_vertex]:
            if min_path[v] > min_path[min_vertex] + w:
                min_path[v] = min_path[min_vertex] + w
                heapq.heappush(min_heap, (min_path[v], v))

    avg = 0
    cnt = 0
    for i in range(n_vertex):
        if min_path[i] != inf and i != s:
            avg += min_path[i]
            cnt += 1

with open("dijkstra.out", "w") as f:
    f.write("Average path length: {:.5}".format(avg/cnt))
