import sys
test_case = int(sys.stdin.readline().rstrip())
score: dict = {'A' : 0, 'B' : 0}
for i in range(test_case):
    A, B = map(int,sys.stdin.readline().split())
    if A==B:continue
    elif A > B: score['A']+=1
    elif B > A: score['B'] +=1
print("%d %d" %(score['A'],score['B']))
