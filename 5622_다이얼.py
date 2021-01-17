import sys
string = sys.stdin.readline().rstrip()
count: int = 0
for s in string:
    if s == 'A' or s == 'B' or s == 'C': count+=3
    elif s == 'D' or s == 'E' or s == 'F': count+=4
    elif s == 'G' or s == 'H' or s == 'I': count+=5
    elif s == 'J' or s == 'K' or s == 'L': count+=6
    elif s == 'M' or s == 'N' or s == 'O': count+=7
    elif s == 'P' or s == 'Q' or s == 'R' or s == 'S': count+=8
    elif s == 'V' or s == 'T' or s == 'U': count+=9
    elif s == 'W' or s == 'X' or s == 'Y' or s == 'Z': count+=10
print(count)
