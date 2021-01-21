# import sys
# N, L = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))
# result: list = []
# for i in range(1, N+1):
#     if i - L + 1 <= 0 :
#         print(min(numbers[0: i+1]), end='')
#     else: print(min(numbers[i - L: i]), end='')

import sys
from collections import deque
window = deque()
N, L = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result: list = []

for i in range(N):
    while window and window[-1][1] > numbers[i]:
        window.pop()
    while window and i - window[0][0] >= L:
        window.popleft()
    window.append([i, numbers[i]])
    result.append(window[0][1])

print(*result)