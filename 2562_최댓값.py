import sys
index: int = 0
max_number: int =0
for i in range(1,10):
    N = int(sys.stdin.readline().rstrip())
    if N > max_number: max_number = N; index = i
print(max_number)
print(index)