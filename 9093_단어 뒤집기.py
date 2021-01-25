import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    line = sys.stdin.readline().split()
    result: str = ""
    for l in line:
        result += l[::-1]+" "
    print(result)