import sys


def getinfix(N, n, exp):
    s = []

    for i in exp:
        if i.isalpha() or i.isnumeric():
            if i == 'x':
                s.insert(0, int(n))
            elif i == 'N':
                s.insert(0, int(N))
            else:
                s.insert(0, int(i))
        else:
            op1 = s.pop(0)
            op2 = s.pop(0)
            if i == '+':
                ans = op2 + op1
            elif i == '*':
                ans = op2 * op1
            else:
                ans = op2 % op1
            s.insert(0, ans)
    return s[0]


for line in sys.stdin:
    if line[0] == '0':
        break
    else:
        inp = line.split()
        # print(inp)
        N, n, inp = inp[0], inp[1], inp[2:]
        #print(N, n, inp)
        #print(getinfix(N, n, inp))
        t, h, c = n, n, 0
        while True:
            t = getinfix(N, t, inp)
            h = getinfix(N, getinfix(N, h, inp), inp)
            #print(t, h)
            if t == h:
                break
        while True:
            t = getinfix(N, t, inp)
            c += 1
            if (t == h):
                break
        print(c)
