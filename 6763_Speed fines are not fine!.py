import sys

limit = int(sys.stdin.readline().rstrip())
speed = int(sys.stdin.readline().rstrip())
score = speed - limit

if score <= 0 :
    print("Congratulations, you are within the speed limit!")
elif score >= 1 and score <= 20:
    print("You are speeding and your fine is $100.")
elif score >= 21 and score <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
