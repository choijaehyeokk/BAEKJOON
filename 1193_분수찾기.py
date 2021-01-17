import sys
X = int(sys.stdin.readline().rstrip())
group: int = 1
cur_sum: int = 1
while cur_sum < X:
    group += 1
    cur_sum += group
group += 1
#짝수 내려오고 홀수 올라감
if group % 2 != 0:
    for i in range(1, group):
        if cur_sum - (group-i)+1 == X: print('{0}/{1}'.format(i, group - i))
else:
    for i in range(1, group):
        if cur_sum - (group-i)+1 == X: print('{0}/{1}'.format(group - i,i))


