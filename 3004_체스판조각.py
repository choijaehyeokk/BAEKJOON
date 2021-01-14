import sys

cut = int(sys.stdin.readline().rstrip())

i : int = 1
j : int = 2

for x in range(1,101):
    if x == cut:
        print(i * j)
        break

    if x % 2 == 0:
        j += 1
    else:
        i += 1