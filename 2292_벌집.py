import sys
N = int(sys.stdin.readline().rstrip())
count, i = 1, 1
while count < N:
    count += i * 6
    i += 1
print(i)