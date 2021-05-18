import sys
N = int(sys.stdin.readline().rstrip())
trops = []
left, right = 1 , 1
for _ in range(N):
    trops.append(int(sys.stdin.readline().rstrip()))

#왼쪽
left_first = trops[0]
for i in range(1, len(trops)):
    if trops[i] > left_first:
        left += 1
        left_first = trops[i]
#오른쪽
right_first = trops[-1]
for i in range(len(trops)-1, -1, -1):
    if trops[i] > right_first:
        right += 1
        right_first = trops[i]

print(left)
print(right)