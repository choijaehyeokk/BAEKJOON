import sys
numbers = list(map(int ,sys.stdin.readline().split()))
count: int = 0
if numbers[0] == 1:
    for i in range(len(numbers)):
        if numbers[i] == i+1: count += 1
    print('ascending' if count == 8 else 'mixed')
elif numbers[0] == 8:
    for i in range(len(numbers)):
        if numbers[i] == 8-i: count += 1
    print('descending' if count == 8 else 'mixed')
else: print('mixed')