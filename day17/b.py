import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
l = ''
with open(fn) as f:
    l = f.read().strip()

x, y = l.split()[-2:]
x1, x2 = [int(n) for n in x[2:-1].split('..')]
y1, y2 = [int(n) for n in y[2:].split('..')]

def check_in(x, y):
    global x1, x2, y1, y2
    if x in range(x1, x2+1):
        if y in range(y1, y2+1):
            return True
    return False

def do_steps(xv, yv):
    global x1, x2, y1, y2
    x, y = 0, 0
    num_steps = 0
    passed = False
    landed = False
    while not passed or landed:
        if x > max(x1, x2) or y < min(y2, y1):
            passed = True
            break
        if check_in(x, y):
            landed = True
            break
        x += xv
        y += yv
        if xv > 0:
            xv -= 1
        yv -= 1
        num_steps += 1
    return landed, passed, num_steps

coords = set()
for xv in range(0, max(x1, x2)+1):
    for yv in range(-500, 500):
        l, p, n = do_steps(xv, yv)
        if l:
            coords.add((xv, yv))
print(len(coords))