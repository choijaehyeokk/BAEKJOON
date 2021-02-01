import sys
N, K = map(int, sys.stdin.readline().split())
numbers = []
result = []
idx: int = 0
for i in range(1, N+1):
    numbers.append(i)
for j in range(N):
    idx = (idx + (K-1)) % len(numbers)
    e = numbers.pop(idx)
    result.append(e)
print('<',end='')
for k in range(len(result)):
    print(result[k], end='')
    if k != len(result)-1: print(', ',end='')
print('>',end='')

#pop() 함수는 고정 되어 있는 deque, list 에서 해당 인덱스의 원소를 뺀다.


