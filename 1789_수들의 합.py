import sys

S = int(sys.stdin.readline().rstrip())
i = 1

while True:
    A = (i * (i + 1)) / 2
    B = ((i+1) * (i+2)) / 2
    if A <= S and  S < B:
        break
    i += 1
print(i)