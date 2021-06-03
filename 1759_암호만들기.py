import  sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alpabets = sys.stdin.readline().rstrip().split(' ')
result = 0
vowel = ['a','e','i','o','u']
alpabets.sort()
for p in list(combinations(alpabets,L)):
    vowel_cnt = 0
    con_cnt = 0
    for v in p:
        if v in vowel:
            vowel_cnt += 1
        else:
            con_cnt += 1
    if vowel_cnt >= 1 and con_cnt >= 2:
        print(''.join(p))
