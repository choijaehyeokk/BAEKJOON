import sys

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

N = int(sys.stdin.readline().rstrip())
person = {}
result = [-1, -1]
for i in range(1, N+1):
    if i not in person:
        person[i] = [int(sys.stdin.readline().rstrip())]
    else:
        person[i].append(int(sys.stdin.readline().rstrip()))

for i in range(1, N+1):
    cnt = len(dfs(person, i))
    if result[1] < cnt:
        result[0], result[1] = i, cnt
print(result[0])