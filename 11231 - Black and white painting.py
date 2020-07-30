import sys

for line in sys.stdin:
    a, b, c = [int(x) for x in line.split()]
    if(a == 0 and b == 0 and c == 0):
        break
    else:
        brd = (a-7)*(b-7)
        if brd % 2 == 1 and c == 1:
            print(brd//2+1)
        else:
            print(brd//2)
