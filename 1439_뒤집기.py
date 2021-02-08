import sys
S = sys.stdin.readline().rstrip()
a_cnt, b_cnt = 0, 0
A = S.split('1')
B = S.split('0')
for a in A:
    if a != '':
        a_cnt += 1
for b in B:
    if b != '':
        b_cnt += 1
print(min(a_cnt, b_cnt))







