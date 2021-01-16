import sys
T = int(sys.stdin.readline().rstrip())

for i in range(T):
    HP, MP, power, defen, A, B, C, D = map(int , sys.stdin.readline().split())
    HP += A
    MP += B
    power += C
    defen += D
    if HP < 1 : HP = 1
    if MP < 1 : MP = 1
    if power < 0 : power = 0
    print(1*HP + 5*MP + 2*power + 2*defen)