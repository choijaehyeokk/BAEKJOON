import sys

count : int = 0
for i in range(6):
    A = sys.stdin.readline().rstrip()
    if A == 'W':
        count += 1

if count == 5 or count == 6:
    print(1)
elif count == 3 or count == 4:
    print(2)
elif count == 2 or count == 1:
    print(3)
else:
    print(-1)



