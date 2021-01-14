import sys

N = int(sys.stdin.readline().rstrip())
fees = list(map(int, sys.stdin.readline().split()))
Y : int =0
M : int = 0
for i in range(N):
     Y += ((fees[i] // 30) + 1) * 10
     M += ((fees[i] // 60) + 1) * 15

if Y < M : print("Y %d" %(Y))
elif M < Y: print("M %d" %(M))
else: print("Y M %d" %(Y))
