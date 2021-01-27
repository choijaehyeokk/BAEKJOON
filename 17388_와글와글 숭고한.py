import sys

univs = list(map(int, sys.stdin.readline().split()))

if sum(univs) >= 100:
    print("OK")
else:
    M = min(univs)
    if M == univs[0]: print("Soongsil")
    elif M == univs[1]: print("Korea")
    else: print("Hanyang")