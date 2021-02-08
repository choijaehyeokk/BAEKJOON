import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    arr = sorted(list(map(int, sys.stdin.readline().split())))
    print(arr[len(arr)-3])