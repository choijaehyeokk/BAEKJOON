import sys
testcase = int(sys.stdin.readline().rstrip())
for test in range(testcase):
    ox = sys.stdin.readline().rstrip()
    result, o = 0, 0
    for i in ox:
        if i == 'X': o = 0
        else:
            o += 1
            result += o
    print(result)
