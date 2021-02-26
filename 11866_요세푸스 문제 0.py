import sys, collections
N, K = map(int,sys.stdin.readline().split())
result = []
numbers = []
idx = 0
for i in range(1, N+1):
    numbers.append(i)

for j in range(N):
    idx = (idx + (K-1)) % len(numbers)
    e = numbers.pop(idx)
    result.append(e)

print('<',end='')
for k in range(len(result)):
    if k == len(result)-1:
        print(result[k],end='')
    else:print(result[k], end=', ')
print('>')

