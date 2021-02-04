import sys

N = int(sys.stdin.readline().rstrip())
number = '666'
idx = 0
i = 1
while True:
    if idx == N: break
    i += 1
    if number in str(i):
        idx += 1

print(i)