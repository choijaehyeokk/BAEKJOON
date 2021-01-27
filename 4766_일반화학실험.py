import sys
previous_temp: float = float(sys.stdin.readline().rstrip())
while True:
    current_temp = float(sys.stdin.readline().rstrip())
    if current_temp == 999: break
    print('%.2f' % (current_temp - previous_temp))
    previous_temp = current_temp
