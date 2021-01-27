import  sys

numbers = list(map(int, list(sys.stdin.readline().split())))

N = numbers[0]
T = numbers[1]
C = numbers[2]
P = numbers[3]
result = 0
for i in range(T, N, T):
    result += (C*P)
print(result)
