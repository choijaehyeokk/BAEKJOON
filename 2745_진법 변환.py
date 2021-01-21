import sys
N, B = sys.stdin.readline().split()
length = len(N)
result: int = 0
dictionary: dict = {''}
for i in range(length-1, -1, -1):
    if N[length-i-1] >= 'A' and N[length-i-1] <= 'Z':
        result += pow(int(B), i) * (ord(N[length - i - 1]) - 55)
    else:
        result += pow(int(B), i) * int(N[length - i - 1])
print(result)
