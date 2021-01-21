import sys
N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline().rstrip())
cnt: int = 0
for i in numbers:
    if v == i: cnt+=1
print(cnt)