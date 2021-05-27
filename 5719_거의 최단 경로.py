import sys,heapq
import collections
def dijkstra(root):
    priority_queue = []
    heapq.heappush(priority_queue,[0, root])
    distance = [sys.maxsize] * (N+1)
    distance[root] = 0

    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)
        if dist > distance[current_node]:
            continue

        for i in graph[current_node]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(priority_queue, [cost, i[0]])
    return distance

def bfs(root, dist):
    #print(dist)
    queue = collections.deque([root])
    shorted_dist = collections.deque()

    while queue:
        current_node = queue.popleft()
        for i in for_bfs_graph[current_node]:
            if i[1] + dist[i[0]] == dist[current_node]:
                queue.append(i[0])
                #shorted_dist.appendleft((i[0],current_node))
                for A in graph[i[0]]:
                    if A[0] == current_node:
                        graph[i[0]].remove(A)
    return shorted_dist

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0: break

    S, D = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for_bfs_graph = [[] for _ in range(N+1)]
    for _ in range(M):
        U, V, P = map(int,sys.stdin.readline().split())
        graph[U].append([V,P])
        for_bfs_graph[V].append([U, P])

    #우선 노드 별로 최단 거리를 구해 준다.
    dist = dijkstra(S)
    #역으로 추적하면서 최단 경로를 그래프에서 제거한다.
    bfs(D, dist)
    #print(graph)
    #다시 다익스트라 알고리즘을 적용해서 최단거리를 구한다.
    dist2 = dijkstra(S)
    #print(dist2)
    if dist2[D] != sys.maxsize:
        print(dist2[D])
    else:
        print(-1)
