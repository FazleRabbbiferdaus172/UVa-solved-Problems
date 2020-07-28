import math
while True:
    n = int(input())
    if(n == 0):
        break
    s = int(n**0.5)
    if s*s == n:
        print("yes")
    else:
        print("no")
