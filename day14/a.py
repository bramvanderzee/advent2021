import sys
from collections import defaultdict

class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None

class LL:
    head = None
    def __init__(self):
        self.head = None

template = ''
pairs = {}
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(fn) as f:
    for l in f:
        l = l.strip()
        if l and l.count('-') > 0:
            a, b = l.split(' -> ', 1)
            pairs[(a[0], a[1])] = b
        elif l:
            template = l

def cycle(ll, pairs):
    n = ll.head
    while n.nxt:
        k = (n.data, n.nxt.data)
        new = Node(pairs[k])
        new.nxt = n.nxt
        n.nxt = new
        n = new.nxt
    return ll

ll = LL()
ll.head = Node(template[0])
prev = ll.head
for d in template[1:]:
    cur = Node(d)
    prev.nxt = cur
    prev = cur

for _ in range(10):
    ll = cycle(ll, pairs)

E = defaultdict(int)
n = ll.head
while True:
    E[n.data] += 1
    if n.nxt:
        n = n.nxt
    else:
        break

print(max(E.values()), min(E.values()))
print(max(E.values()) - min(E.values()))
