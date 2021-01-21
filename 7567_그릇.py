import sys

plate = sys.stdin.readline().rstrip()
result: int = 10
for i in range(1, len(plate)):
    if plate[i] != plate[i-1] : result += 10
    else: result+= 5
print(result)