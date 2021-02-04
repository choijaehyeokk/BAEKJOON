import sys
scores = []
sum = 0
for i in range(1, 9):
    scores.append([i,int(sys.stdin.readline().rstrip())])

scores = sorted(scores, key=lambda x:x[1])[3:]
scores = sorted(scores, key=lambda x:x[0])

for v in scores:
    sum += v[1]
print(sum)
for i in scores:
    print(i[0], end=' ')
