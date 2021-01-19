import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = [1] * N

    for i in range(2, N+1):
        for j in range(N):
            if (j+1) % i == 0:
                if arr[j] == 0: arr[j] = 1
                else: arr[j] = 0
    print(sum(arr))
