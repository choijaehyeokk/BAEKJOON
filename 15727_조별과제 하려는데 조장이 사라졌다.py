import sys
import math

number = int(sys.stdin.readline().split()[0])

print(math.ceil(number/5))

#math.ceil() -> 올림
#math.floor() -> 버림
#math.round() -> 반올림