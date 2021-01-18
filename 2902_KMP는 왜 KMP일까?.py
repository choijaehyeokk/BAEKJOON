import sys
string = sys.stdin.readline().split('-')
result: str = ''
for i in range(len(string)):
    result += string[i][0]
print(result)