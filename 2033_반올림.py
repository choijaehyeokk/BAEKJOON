import sys
N = sys.stdin.readline().rstrip()

def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num)+1
    else:
        return int(num)

i: int = 1
while int(N) > pow(10, i):
    N = (roundUp(int(N) / pow(10, i)) * pow(10, i))
    i += 1
print(N)