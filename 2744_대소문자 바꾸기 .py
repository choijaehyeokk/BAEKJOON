import sys
string = sys.stdin.readline().rstrip()
result: list = []
for i in range(len(string)):
    if string[i].islower():
        result.append(string[i].upper())
    else:
        result.append(string[i].lower())
print(''.join(result))