import sys
T = int(sys.stdin.readline().rstrip())
cal: list = [0] * 100
def isValid(N: int)->int:

    for i in range(1, 100):
        for j in range(1, 100):
            for k in range(1, 100):
                if cal[i] + cal[j] + cal[k] == N:
                    return 1
    return 0

for i in range(len(cal)):
    cal[i] = (i+1)*i / 2

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(isValid(N))