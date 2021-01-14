import sys
N , T = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))
total_time: int = 0
if sum(times) > T:
    for i in range(N):
        total_time += times[i]
        if total_time > T: print(i); break
else: print(N)

