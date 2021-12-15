import sys

M = {}
x, y = 0, 0
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        for c in l.strip():
            M[(x, y)] = int(c)
            x += 1
        x = 0
        y += 1
w, h = max([n for n, _ in M.keys()]), max([n for _, n in M.keys()])

lows = {}
for k, v in M.items():
    x, y = k
    lowest = True
    for dy in [-1, 1]:
        if y+dy >= 0 and y+dy <= h:
            if M[(x, y+dy)] <= v:
                lowest = False
    for dx in [-1, 1]:
        if x+dx >= 0 and x+dx <= w:
            if M[(x+dx, y)] <= v:
                lowest = False
    if lowest:
        lows[k] = v

print(sum([n+1 for n in lows.values()]))