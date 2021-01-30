import sys
N = int(sys.stdin.readline().rstrip())
arr1, arr2 = [0] * 3, [0] * 3

for _ in range(N):
    A, B, C = map(int, sys.stdin.readline().split())
    arr1[0] += A
    arr1[1] += B
    arr1[2] += C

    arr2[0] += A*A
    arr2[1] += B*B
    arr2[2] += C*C

value = max(arr1)
if arr1.count(value) == 1:
    for i in range(len(arr1)):
        if arr1[i] == value: print(i+1, value)
else:
    max_value = max(arr2)
    if arr2.count(max_value) > 1:
        print(0, value)
    else:
        for i in range(len(arr2)):
            if arr2[i] == max_value:
                print(i+1, value)
