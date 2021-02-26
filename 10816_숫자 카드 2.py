import sys
from collections import Counter
N = int(sys.stdin.readline().rstrip())
n_num = Counter(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline().rstrip())
m_num = list(map(int, sys.stdin.readline().split()))

for m in range(len(m_num)):
    if m == len(m_num)-1:
        print(n_num[m_num[m]])
    else: print(n_num[m_num[m]],end=' ')