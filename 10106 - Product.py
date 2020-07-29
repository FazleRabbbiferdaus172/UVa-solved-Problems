import sys
mul = 1
for i, x in enumerate(sys.stdin):
    mul = mul*int(x)
    if i > 0 and i % 2 == 1:
        print(mul)
        mul = 1
