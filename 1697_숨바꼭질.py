import sys, collections

def bfs(start, end):
    queue = collections.deque([start])
    result = [0] * 100001
    while queue:
        current = queue.popleft()
        if current == end:
            return result[end]
        for e in (current - 1, current + 1, current *2):
            if 0 <= e < 100001 and result[e] == 0:
                result[e] = result[current] + 1
                queue.append(e)

N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))
