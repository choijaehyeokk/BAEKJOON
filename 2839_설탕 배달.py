import sys
N = int(sys.stdin.readline().rstrip())

def cal(N: int):
    cnt: int = 0
    re = N
    if N % 5 == 0: return N//5

    while N > 0:
        N -= 3
        cnt+=1
        if N % 5 == 0:
            cnt += N//5
            return cnt
    return -1

print(cal(N))