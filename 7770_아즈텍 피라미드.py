import sys
N =  int(sys.stdin.readline().rstrip())
block: int = 0
i: int = 0
while block <= N:
    block = 2*pow(i,2) + 2*i + 1
    i+=1
print(i-1)
#N = (2n-1)^2 - (2n-1)

