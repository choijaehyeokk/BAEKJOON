import sys
count = int(sys.stdin.readline().rstrip())
j : int = count
for i in range(count):
    print(i*' ' + (j*2 -1) * '*')
    j -=1