import sys

N = int(sys.stdin.readline().rstrip())
first = True
result = []
for i in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    numbers = list(str(input[0]))
    s_num = input[1]
    b_num = input[2]
    if i != 0: first = False

    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                strike, ball = 0 , 0
                if a == b or b == c or a == c: continue

                if numbers[0] == str(a):
                    strike += 1
                elif str(a) in numbers and numbers[0] != str(a):
                    ball += 1

                if numbers[1] == str(b):
                    strike += 1
                elif str(b) in numbers and numbers[1] != str(b):
                    ball += 1

                if numbers[2] == str(c):
                    strike += 1
                elif str(c) in numbers and numbers[2] != str(c):
                    ball += 1

                if str(a) + str(b) + str(c) not in result and strike == s_num and ball == b_num and first:
                    result.append(str(a) + str(b) + str(c))

                if str(a) + str(b) + str(c) in result and (strike != s_num or ball != b_num) and not first:
                    result.remove(str(a) + str(b) + str(c))


print(len(result))
