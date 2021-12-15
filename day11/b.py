import sys
from collections import deque

octopi = {}
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for y, l in enumerate(f):
        for x, o in enumerate(l.strip()):
            octopi[(x, y)] = int(o)

def cycle(octopi):
    # increase all by 1
    octopi = {k:v+1 for k,v in octopi.items()}

    Q = deque()
    F = []
    # e > 9: flash, surrounding +1. repeat
    for k, v in octopi.items():
        if v > 9:
            Q.append(k)
            F.append(k)
    
    while Q:
        x, y = Q.pop()
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if (x+dx, y+dy) in octopi.keys():
                    k = (x+dx, y+dy)
                    octopi[k] += 1
                    if octopi[k] == 10:
                        Q.append(k)
                        F.append(k)

    # flashed? e = 0
    for k in F:
        octopi[k] = 0
    
    return octopi, len(F)

steps = 0
while True:
    steps += 1
    octopi, n = cycle(octopi)
    if len(octopi) == n:
        break
print(steps)