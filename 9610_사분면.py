import sys

N = int(sys.stdin.readline().rstrip())
quantile: dict = {'Q1':0, 'Q2':0, 'Q3':0, 'Q4':0, 'AXIS':0}
for i in range(N):
    X,Y = map(int, sys.stdin.readline().split())
    if X == 0 or  Y == 0 :
        quantile['AXIS'] += 1
        continue

    if X < 0 and Y < 0 : quantile['Q3'] += 1
    elif X > 0 and Y > 0 : quantile['Q1'] += 1
    elif X > 0 and Y < 0 : quantile['Q4'] += 1
    elif X < 0 and Y > 0 : quantile['Q2'] += 1
for k ,v in quantile.items():
    print("{0}: {1}".format(k, v))