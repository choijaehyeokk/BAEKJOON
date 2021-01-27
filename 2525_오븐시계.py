import sys

numbers = list(map(int, sys.stdin.readline().split()))

time = int(sys.stdin.readline().rstrip())
hour: int = numbers[0]
minute: int = numbers[1]

hour += (time // 60)
minute += (time % 60)

if minute >= 60 :
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24

print(hour, minute)