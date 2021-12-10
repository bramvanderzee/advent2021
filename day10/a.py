import sys
from collections import deque

complement = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '<': '>',
    '>': '<'
}

values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

lines = []
fn = sys.argv[1] if len(sys.argv)  > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        lines.append(l.strip())

points = 0
for line in lines:
    Q = deque()
    corrupt = False
    for c in line:
        if corrupt:
            break
        if c not in values.keys():
            Q.append(c)
        else:
            v = Q.pop()
            if c != complement[v]:
                points += values[c]
                corrupt = True
print(points)