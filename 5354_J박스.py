import sys

test_case = int(sys.stdin.readline().rstrip())
for i in range(test_case):
    N = int(sys.stdin.readline().rstrip())
    if N == 1: print('#')
    else:
        print('#'*N)
        for j in range(N-2):
            print('#'+ 'J'* (N-2) + '#')
        print('#'*N)
    if i == test_case-1: break
    print()