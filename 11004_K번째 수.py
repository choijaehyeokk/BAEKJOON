import sys
N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
num_dict = {}
cnt: int =0
for n in numbers:
    if n in num_dict:
        num_dict[n] += 1
    else:
        num_dict[n] = 1

num_dict = sorted(num_dict.items())
for A in num_dict:
    for j in range(1, A[1]+1):
        cnt += 1
        if cnt == K: print(A[0]); break