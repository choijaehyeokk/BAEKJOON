while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break

'''
input은 EOF를 받을 때 EOFError를 일으키지만 

sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴한.

따라서 오류가 발생하지 않고 틀린다..
'''