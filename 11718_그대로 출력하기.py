import sys
for i in range(100):
    try:
        string = sys.stdin.readline().rstrip()
        print(string)
    except EOFError: break