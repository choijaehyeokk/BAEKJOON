import sys
AB = list(map(int,sys.stdin.readline().split()))
CD = list(map(int,sys.stdin.readline().split()))
abcd: list = AB + CD
current_max: int = -sys.maxsize
result: int = 0
for i in range(3):
    current_max = max(current_max, abcd[0]/abcd[2] + abcd[1]/abcd[3])
    abcd[0],abcd[1],abcd[2],abcd[3] = abcd[2], abcd[0], abcd[1], abcd[3]
    if current_max < abcd[0]/abcd[2] + abcd[1]/abcd[3]:
        result = i+1
print(result)

