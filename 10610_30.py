import sys
N = list(str(int(sys.stdin.readline().rstrip())))
N = sorted(N, reverse=True)

if sum(map(int, N)) % 3 != 0 or N[len(N)-1] != '0':
    print(-1)
else:
    print(int(''.join(N)))