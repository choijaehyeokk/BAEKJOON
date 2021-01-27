import sys
count = int(sys.stdin.readline().rstrip())
j : int = 1
for i in range(count-1):
    print(' ' * (count-i-1) + '*'*j)
    j+=2
print('*' * j)
j-=2
for i in range(count-1):
    print(' ' * (i+1) + '*' *j)
    j-=2