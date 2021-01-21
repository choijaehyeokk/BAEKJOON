import sys

string = sys.stdin.readline().rstrip()
doctor = sys.stdin.readline().rstrip()

print('go' if len(string) >= len(doctor) else 'no')