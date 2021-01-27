import sys
gimbob: list = []
seven_25 = list(map(int,sys.stdin.readline().split()))
gimbob.append(seven_25)
test_case = int(sys.stdin.readline().rstrip())

for i in range(test_case):
    shops = list(map(int,sys.stdin.readline().split()))
    gimbob.append(shops)
for i in range(len(gimbob)):
    price = (1000 / gimbob[i][1]) * gimbob[i][0]
    gimbob[i] = price
print(min(gimbob))