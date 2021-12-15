import sys
from collections import defaultdict, deque
import queue

D = {
    (0, 1): 'N',
    (1, 0): 'E',
    (0, -1): 'S',
    (-1, 0): 'W'
}

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
        return self.gt < other.gt
    
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
                        cost -= 9
                    M[(x + dx * W, y + dy * H)] = Node(x + dx * W, y + dy * H, int(cost))
print('Size:', mx, my)

def calc_heuristic(from_c, to_c) -> int:
    x1, y1 = from_c
    x2, y2 = to_c
    return pow(x2-x1, 2)+pow(y2-y1, 2) # euclidian distance

print('Getting adjacents...')
for node in M.values():
    node.h = calc_heuristic((node.x, node.y), (mx, my))
    adj = []
    for dy in [-1, 1]:
        c = (node.x, node.y + dy)
        if c in M:
            adj.append(M[c])
    for dx in [-1, 1]:
        c = (node.x + dx, node.y)
        if c in M:
            adj.append(M[c])
    node.adj.extend(adj)

print('Calculating route...')
M[(0, 0)].gt = 0
seen = defaultdict(bool)
open_nodes = queue.PriorityQueue()
open_nodes.put((0, M[(0, 0)]))
closed_nodes = []
while open_nodes:
    _, node = open_nodes.get()
    closed_nodes.append(node)
    print(node.x, node.y)
    seen[(node.x, node.y)] = True
    if node == M[(mx, my)]:
        break
    adj = [n for n in node.adj if not seen[(n.x, n.y)]]
    for n in adj:
        if n.gt:
            if n.gt < node.gt + n.g:
                continue
        n.gt = node.gt + n.g
        open_nodes.put((n.gt, n))

print('Calculating cost')
print(M[(mx, my)].gt)