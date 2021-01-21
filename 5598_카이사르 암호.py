import sys

before = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z' ]
string = sys.stdin.readline().rstrip()
result = ''
for i in range(len(string)):
    result += before[before.index(string[i])-3]
print(result)