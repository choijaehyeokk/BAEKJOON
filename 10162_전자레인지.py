import sys

time = int(sys.stdin.readline().rstrip())
f_minute : int = 0
o_minute : int = 0

f_minute = int(time // 300)
time -= (f_minute*300)

o_minute = int(time // 60)
time -= (o_minute*60)

if time % 10 == 0:
    print(f_minute, o_minute, int(time // 10))
else:
    print(-1)

