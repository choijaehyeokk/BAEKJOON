import sys
N = int(sys.stdin.readline().rstrip())
input_divs = list(map(int, sys.stdin.readline().split()))
input_divs.sort()
print(input_divs[0] * input_divs[len(input_divs)-1])