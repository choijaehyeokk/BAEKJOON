import sys

two_numbers = list(map(int,list(sys.stdin.readline().split())))
print(sum(two_numbers)*(two_numbers[0]-two_numbers[1]))

#(A+B)×(A-B)
