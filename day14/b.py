import sys
from collections import defaultdict, Counter

class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

class LL:
    head = None
    def __init__(self):
        self.head = None

template = ''
P = {}
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        l = l.strip()
        if l and l.count('-') > 0:
            a, b = l.split(' -> ', 1)
            P[a] = b
        elif l:
            template = l

def cycle(pairs, P):
    new_pairs = defaultdict(int)
    for p, v in pairs.items():
        p1, p2 = p[0] + P[p], P[p] + p[1]
        new_pairs[p1] += v
        new_pairs[p2] += v
    return new_pairs

pairs = defaultdict(int)
for i in range(1, len(template)):
    pairs[template[i-1] + template[i]] += 1

for _ in range(10):
    pairs = cycle(pairs, P)

print(pairs)
C = defaultdict(int)
for n, v in pairs.items():
    C[n[0]] += v
C[n[1]] += v
print(max(C.values()), min(C.values()))
print(max(C.values()) - min(C.values()))