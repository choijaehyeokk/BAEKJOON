import sys
while True:
    test: dict = {'factor': 0, 'multiple': 0, 'neither': 0}
    N, M = map(int, sys.stdin.readline().split())
    if N==0 and M == 0 : break

    if N > M and N % M == 0 and (N // M) * M == N : test['multiple'] = 1
    elif N < M and M % N == 0 and (M // N) * N == M : test['factor'] = 1
    else: test['neither'] = 1
    print([k for k, v in test.items() if v == 1][0])
    test.clear()

