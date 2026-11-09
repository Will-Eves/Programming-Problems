import random

# bool(random.getrandbits(1))

r, c = map(int, input().split())

for y in range(r):
    o = ''
    for x in range(c):
        if bool(random.getrandbits(1)):
            o += '*'
        else:
            o += '.'
    
    print(o)