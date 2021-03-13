import sys
N = int(sys.stdin.readline().rstrip())
times = list(map(int ,sys.stdin.readline().split()))
times = sorted(times)
result = [0 for _ in range(N+1)]
for i in range(N):
    result[i+1] = times[i] + result[i]
print(sum(result))