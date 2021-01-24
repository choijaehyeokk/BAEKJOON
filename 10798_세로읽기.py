import sys
lines: list =[]
result: str = ""
i : int = 0
cnt: int = 0
for _ in range(5):
    lines.append(sys.stdin.readline().rstrip())

while i < 15:
    for l in lines:
        if len(l) <= i:
            continue
        result += l[i]
    i+=1
print(result)