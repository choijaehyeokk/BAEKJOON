import sys

result : int =0
for i in range(3):
    yoot = list(map(int, sys.stdin.readline().split()))
    for j in range(len(yoot)):
        if yoot[j] == 1:
            result += 1
    if result == 0: print('D')
    elif result == 1: print('C')
    elif result == 2: print('B')
    elif result == 3: print('A')
    elif result == 4: print('E')
    result = 0