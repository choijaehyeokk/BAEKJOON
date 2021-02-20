import sys

N = int(sys.stdin.readline().rstrip())
result : int = 0

def is_han(n: int)->bool:
    A = list(str(n))
    if len(A) == 1: return True
    else:
        d = int(A[1]) - int(A[0])
        for i in range(len(A)-1):
            if d != int(A[i+1]) - int(A[i]):
                return False
    return True

for i in range(1, N+1):
    if is_han(i): result += 1
print(result)