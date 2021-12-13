import sys

folds = []
dots = {}
w, h = 0, 0
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        t = l.strip()
        if t.startswith('fold along'):
            d, p = t.split()[-1].split('=', 1)
            folds.append((d, int(p)))
        elif len(l) > 1:
            x, y = [int(n) for n in t.split(',')]
            w = max(w, x)
            h = max(h, y)
            dots[(x, y)] = '#'

def do_fold(M, d, p, w, h):
    new_M = {}
    if d == 'x':
        w = p
        for k, v in M.items():
            x, y = k
            if x < p:
                new_M[k] = v
            if x > p:
                new_M[(2*p - x, y)] = '#'
    else:
        h = p
        for k, v in M.items():
            x, y = k
            if y < p:
                new_M[k] = v
            if y > p:
                new_M[(x, 2*p - y)] = '#'
    return new_M, w, h

d, p = folds.pop(0)
dots, w, h = do_fold(dots, d, p, w, h)
count = 0
M = [['#' if (x, y) in dots.keys() else '.' for x in range(w+1)] for y in range(h+1)]
for y in M:
    for x in y:
        print(x, end='')
    print()
print(len([n for n in dots.values() if n == '#']))