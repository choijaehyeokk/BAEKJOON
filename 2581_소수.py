import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
nums = []
for i in range(M, N+1):
    flag = True
    if i == 1: continue
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True: nums.append(i)

if nums:
    print(sum(nums))
    print(min(nums))
else: print(-1)