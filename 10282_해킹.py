import sys, heapq
import collections

Test_case = int(sys.stdin.readline().rstrip())

def dijkstra(N, root):
    priority_queue = []
    current_lower = [int(sys.maxsize)]* (N+1)
    current_lower[root] = 0
    heapq.heappush(priority_queue, (0, root))

    cnt = 0
    max_dist = -1
    while priority_queue:
        dist, current_node = heapq.heappop(priority_queue)
        if current_lower[current_node] < dist:
            continue

        for i in graph[current_node]:
            cost = dist + i[1]
            if current_lower[i[0]] > cost:
                current_lower[i[0]] = cost
                heapq.heappush(priority_queue, (cost, i[0]))
    print(current_lower)
    for i in current_lower:
        if i == sys.maxsize:
            continue
        else:
            cnt += 1
            if max_dist < i:
                max_dist = i
    return cnt, max_dist

for _ in range(Test_case):
    n, d, c = map(int, sys.stdin.readline().split())
    #n: 컴퓨터수 , d: 의존성 개수, c: 해킹당한 컴퓨터
    graph = [[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append([a,s])
    print(*dijkstra(n,c))