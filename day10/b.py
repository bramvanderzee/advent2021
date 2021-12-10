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
    
values = {k:v+1 for v, k in enumerate([')', ']', '}', '>'])}

lines = []
fn = sys.argv[1] if len(sys.argv)  > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        lines.append(l.strip())

incomplete = []
for line in lines:
    Q = deque()
    corrupt = False
    for c in line:
        if corrupt:
            break
        if c in ['(', '[', '{', '<']:
            Q.append(c)
        else:
            v = Q.pop()
            if c != complement[v]:
                corrupt = True
    if not corrupt:
        incomplete.append(line)

P = []
for line in incomplete:
    Q = deque()
    for c in line:
        if c in ['(', '[', '{', '<']:
            Q.append(c)
        else:
            v = Q.pop()
    points = 0
    for c in reversed(Q):
        points *= 5
        points += values[complement[c]]
    P.append(points)
print(sorted(P)[len(P)//2])