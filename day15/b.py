import sys
from collections import defaultdict, deque
import queue

sys.setrecursionlimit(int(1e6))

class Node:
    def __init__(self, x, y, g):
        self.x = x
        self.y = y
        self.g = g
        self.gt = None
        self.h = None
        self.adj = []
    
    def cost(self):
        if self.h and self.gt:
            return self.gt + self.h
        else:
            return self.g

    def __lt__(self, other):
        return self.cost() < other.cost()
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
M = {}
mx, my = None, None
with open(fn) as f:
    lines = f.readlines()
    H = len(lines)
    for y, l in enumerate(lines):
        W = len(l.strip())
        if not mx:
            mx, my = W * 5 - 1, H * 5 - 1
        for x, c in enumerate(l.strip()):
            for dy in range(5):
                for dx in range(5):
                    cost = int(c)
                    cost += dx + dy
                    if cost > 9:
                        cost = cost%9
                    M[(x + dx * W, y + dy * H)] = int(cost)
print('Size:', mx, my)

def calc_heuristic(from_c, to_c) -> int:
    x1, y1 = from_c
    x2, y2 = to_c
    return (pow(x2-x1, 2)+pow(y2-y1, 2))//100

H = {}
print('Calculating heuristics...')
for k, v in M.items():
    x, y = k
    H[k] = calc_heuristic((x, y), (mx, my))

C = defaultdict(lambda: int(1e9))
print('Calculating route...')
def step(state):
    global M,C
    node, path = state
    new_path = set(path)
    new_path.add(node)
    
    cost = 0
    for n in new_path:
        cost += M[n]
    if cost < C[node]:
        C[node] = cost

    print(node, C[node])

    if node == (mx, my):
        print(C[node])
        sys.exit()

    adj = []
    x, y = node
    for dy in [-1, 1]:
        c = (x, y + dy)
        if c in M:
            adj.append(c)
    for dx in [-1, 1]:
        c = (x + dx, y)
        if c in M:
            adj.append(c)

    to_search = sorted(set(adj) - new_path, key=lambda c: H[c])
    for n in to_search:
        step((n, new_path))

step(((0, 0), []))