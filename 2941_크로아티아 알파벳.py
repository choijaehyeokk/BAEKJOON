import sys
croa_dict = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=', 'z=']
string = sys.stdin.readline().rstrip()
i: int = 0
result: int = 0

while i < len(string):
    if string[i] == 'd' and string[i:i+3] in croa_dict:
        i += 2
        result += 1
    elif string[i:i+2] in croa_dict:
        i += 1
        result += 1
    else:
        result += 1
    i += 1
print(result)