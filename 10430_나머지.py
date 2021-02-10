import sys

input_number = list(map(int, list(sys.stdin.readline().split())))

# TODO 1 : (A+B)%C
print((input_number[0]+input_number[1])%input_number[2])
# TODO 2 : ((A%C) + (B%C))%C
print(((input_number[0]%input_number[2]) + (input_number[1]%input_number[2]))%input_number[2])
# TODO 3 : (A×B)%C
print((input_number[0]*input_number[1])%input_number[2])
# TODO 4 : (A%C) × (B%C))%C
print(((input_number[0]%input_number[2]) * (input_number[1]%input_number[2]))%input_number[2])


