import sys

persons = int(sys.stdin.readline().rstrip())
result: int = 0

for i in range(1, persons-2):
    for j in range(i+1, persons-1):
        for k in range(j+1,persons):
            result+=1

print(result)