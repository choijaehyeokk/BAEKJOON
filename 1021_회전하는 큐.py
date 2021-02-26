import sys
import collections

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
dq = collections.deque()
cnt = 0
for i in range(1, N+1):
    dq.append(i)

for n in numbers:
    if dq[0] == n:
        dq.popleft()
    elif len(dq) // 2 >= dq.index(n):
        while dq[0] != n:
            dq.append(dq[0])
            dq.popleft()
            cnt += 1
        dq.popleft()
    else:
        while dq[0] != n:
            dq.appendleft(dq[-1])
            dq.pop()
            cnt += 1
        dq.popleft()
print(cnt)
