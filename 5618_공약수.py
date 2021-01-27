import sys


testcase = int(sys.stdin.readline().rstrip())
if testcase == 2: A,B = map(int,sys.stdin.readline().split())
elif testcase == 3: A,B,C = map(int,sys.stdin.readline().split())

for i in range(1, A+1):
    if testcase ==  2:
        if A % i == 0 and B % i == 0: print(i)
    elif testcase == 3:
        if A % i == 0 and B % i == 0 and C % i == 0: print(i)

# def gcd(x: int, y: int) -> int:
# 	if y == 0 : return x
# 	else: return gcd(y, x % y)
#
#
# testcase = int(sys.stdin.readline().rstrip())
# numbers = list(map(int, sys.stdin.readline().split()))
# A,B,C, result = [], [], [], []
#
# if testcase == 2:
#     for i in range(1, gcd(numbers[0],numbers[1])+1):
#         if numbers[0] % i == 0: A.append(i)
#         if numbers[1] % i == 0: B.append(i)
#     result = [value for value in A if value in B]
# elif testcase == 3:
#     numbers = sorted(numbers)
#     for i in range(1, gcd(numbers[2],gcd(numbers[1],numbers[0]))+1):
#         if numbers[0] % i == 0: A.append(i)
#         if numbers[1] % i == 0: B.append(i)
#         if numbers[2] % i == 0: C.append(i)
#     result = [value for value in A if value in B and value in C]
# for value in result:
#     print(value)

