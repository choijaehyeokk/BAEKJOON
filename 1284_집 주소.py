import sys

while True:
    N = sys.stdin.readline().rstrip()
    if N == '0': break

    total : int = 0
    length = len(N)
    for i in range(length):
        if N[i] == '1': total += 2
        elif N[i] == '0': total += 4
        else: total += 3
    total += length + 1
    print(total)