import sys, collections
A, B = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline().rstrip())
num = list(map(int ,sys.stdin.readline().split()))
dec: int = 0
result = collections.deque()
for i in range(M):
    dec += num[i]*pow(A, M - (i+1))

while dec >= B:
    result.appendleft(dec % B)
    dec = dec // B
result.appendleft(dec)
print(*result)