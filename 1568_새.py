import sys

N =int(sys.stdin.readline().rstrip())
start = 1
count = 0
while N > 0:
    if start > N:
        start = 1

    N -= start
    start += 1
    count += 1

print(count)