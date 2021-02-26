import sys, collections
graph_list = {}
def dfs(graph: dict, root: int): #stack 자료구조를 사용한다.
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                stack += sorted(list(set(graph[n]) - set(visited)), reverse=True)
    return visited

def bfs(graph: dict, root: int): #queue 자료구조를 사용한다.
    visited = []
    queue = collections.deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                queue += sorted(list(set(graph[n]) - set(visited)))
    return visited

N, M, V = map(int, sys.stdin.readline().split())
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    if v1 not in graph_list:
        graph_list[v1] = [v2]
    elif v1 in graph_list:
        graph_list[v1].append(v2)

    if v2 not in graph_list:
        graph_list[v2] = [v1]
    elif v2 in graph_list:
        graph_list[v2].append(v1)
print(graph_list)
print(*dfs(graph_list, V))
print(*bfs(graph_list, V))
