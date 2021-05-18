#case 1 : backtracking algorithm
import sys
N, M = map(int ,sys.stdin.readline().split())
visited = [False] * N
result = []

def solve(depth, N, M):
    if depth == M:
        print(*result)
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            result.append(i+1)
            solve(depth+1, N, M)

            visited[i] = False
            result.pop()

solve(0, N, M)

#case 2 : permutaions 사용
'''
from itertools import permutations
import sys
N, M = map(int, sys.stdin.readline().split())
P = permutations(range(1, N+1), M)
for i in P:
    print(*i)
'''