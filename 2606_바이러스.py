import sys, collections

def bfs(graph, root):
    cnt = 0
    visited = []
    queue = collections.deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                queue += sorted(list(set(graph[n]) - set(visited)))
                cnt += 1
    #print(visited)
    return cnt-1

computers = int(sys.stdin.readline().rstrip())
nodes = int(sys.stdin.readline().rstrip())
graph_list = {}
for _ in range(nodes):
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 not in graph_list:
        graph_list[v1] = [v2]
    elif v1 in graph_list:
        graph_list[v1].append(v2)

    if v2 not in graph_list:
        graph_list[v2] = [v1]
    elif v2 in graph_list:
        graph_list[v2].append(v1)

print(bfs(graph_list,1))
