import sys
count = int(sys.stdin.readline().rstrip())
j : int = 2*count -1
for i in range(count-1):
    print(' '* i + '*' * j)
    j-=2
print(' '*(count-1) + '*')
j+=2
for i in range(count-1):
    print(' '*(count-i-2) + '*'*j)
    j+=2