import sys

two_number = list(map(int, list(sys.stdin.readline().split())))

print(two_number[0]+two_number[1])
print(two_number[0]-two_number[1])
print(two_number[0]*two_number[1])
print(two_number[0]//two_number[1])
print(two_number[0]%two_number[1])