import sys
import math
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

def get_points(c1, c2):
    points = [c1, c2]
    x1, y1 = c1
    x2, y2 = c2
    dx, dy = x2 - x1, y2 - y1
    gcd = math.gcd(dx, dy)
    dx, dy = int(dx/gcd), int(dy/gcd)
    for d in range(1, gcd):
        cx, cy = x1 + (dx * d), y1 + (dy * d)
        points.append((cx, cy))
    return points

max_x, max_y = 0, 0
lines = []
with open(fn) as f:
    for l in f:
        c1, c2 = l.strip().split(' -> ', 1)
        c1 = tuple([int(n) for n in c1.split(',', 1)])
        c2 = tuple([int(n) for n in c2.split(',', 1)])
        lines.append([c1, c2])
        x1, y1 = c1
        x2, y2 = c2
        if max(x1, x2) > max_x:
            max_x = max(x1, x2)
        if max(y1, y2) > max_y:
            max_y = max(y1, y2)

chart = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for line in lines:
    c1, c2 = line
    x1, y1 = c1
    x2, y2 = c2
    if x1 == x2 or y1 == y2:
        points = get_points(c1, c2)
        for point in points:
            x, y = point
            chart[y][x] += 1

count = 0
for line in chart:
    for c in line:
        print(c, end=' ')
        if c > 1:
            count += 1
    print()
print(count)