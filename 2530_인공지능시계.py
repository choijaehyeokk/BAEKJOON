import sys

numbers = list(map(int, sys.stdin.readline().split()))

time = int(sys.stdin.readline().rstrip())
hour: int = numbers[0]
minute: int = numbers[1]
seconds : int = numbers[2]

hour += (time // 3600)
minute += ((time%3600) // 60)
seconds += ((time%3600) % 60)

if seconds >= 60:
    minute += 1
    seconds -= 60
if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour = hour % 24

print(hour, minute, seconds)