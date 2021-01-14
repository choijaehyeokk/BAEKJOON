import sys

day = int(sys.stdin.readline().rstrip())
cars = list(map(int, list(sys.stdin.readline().split())))
count : int = 0
for i in range(5):
    if day == cars[i]:
        count += 1

print(count)