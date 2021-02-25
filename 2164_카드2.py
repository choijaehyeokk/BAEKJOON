import sys, collections
Dq = collections.deque()
N = int(sys.stdin.readline().rstrip())
T = 1
for i in range(1, N+1):
    Dq.append(i)

while len(Dq) != 1:
    if T % 2 == 0:
        Dq.append(Dq[0])
        Dq.popleft()
    else:
        Dq.popleft()
    T += 1

print(Dq[0])