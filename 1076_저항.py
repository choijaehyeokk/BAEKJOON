import sys
A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
C = sys.stdin.readline().rstrip()

# black	0	1
# brown	1	10
# red	2	100
# orange	3	1000
# yellow	4	10000
# green	5	100000
# blue	6	1000000
# violet	7	10000000
# grey	8	100000000
# white	9	1000000000
reg: dict = {'black' : {'value' : '0', 'mul' : 1},
             'brown' : {'value' : '1', 'mul' : 10},
             'red' : {'value' :'2', 'mul': 100},
             'orange' : {'value' :'3', 'mul': 1000},
             'yellow' : {'value' : '4', 'mul': 10000},
             'green' : {'value' : '5', 'mul': 100000},
             'blue' : {'value' : '6', 'mul': 1000000},
             'violet' : {'value' : '7', 'mul': 10000000},
             'grey' : {'value' : '8', 'mul': 100000000},
             'white' : {'value' : '9', 'mul': 1000000000},
             }
print(int(reg[A]['value'] + reg[B]['value']) * reg[C]['mul'])