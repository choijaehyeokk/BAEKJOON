import sys
testcase = int(sys.stdin.readline().rstrip())
for test in range(testcase):
    input_string = sys.stdin.readline().split()
    R,S = int(input_string[0]), input_string[1]
    answer: str = ''
    for s in S:
        answer += s*R
    print(answer)
