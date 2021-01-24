import sys, string

line = sys.stdin.readline().rstrip()
alpabets: list  = [list(string.ascii_lowercase), list(string.ascii_uppercase)]
result: str = ""
for i in range(len(line)):
    if line[i].isupper():
        d = alpabets[1].index(line[i])
        if d > 12: d -= 13; result += alpabets[1][d]
        else: d+=13; result+= alpabets[1][d]
    elif line[i].islower():
        d = alpabets[0].index(line[i])
        if d > 12: d -= 13; result += alpabets[0][d]
        else: d += 13; result += alpabets[0][d]
    else:
        result += line[i]
print(result)