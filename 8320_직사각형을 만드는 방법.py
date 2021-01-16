import sys, math
N = int(sys.stdin.readline().rstrip())
result: int = 0
for i in range(1, N+1):
    for j in range(1, i+1):
        if i * j <= N: result+=1
        else: break
print(result)

# divisor: list = []
# if N == 1: print(1)
# else:
#     for i in range(1, N+1):
#         for j in range(1, i+1):
#             if i % j == 0:
#                 divisor.append(j)
#         result += math.ceil(len(divisor) / 2)
#         divisor.clear()
#     print(result)