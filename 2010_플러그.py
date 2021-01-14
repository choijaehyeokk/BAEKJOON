import sys

N = int(sys.stdin.readline().rstrip())
multi_taps =[]
for i in range(N):
    multi_tap = int(sys.stdin.readline().rstrip())
    multi_taps.append(multi_tap)
print(sum(multi_taps) - N + 1)