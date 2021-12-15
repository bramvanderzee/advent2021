import sys
from collections import deque

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
        if self.h:
            return self.g * 5 + self.h
        else:
            return self.g * 5

    def __lt__(self, other):
        return self.gt < other.gt
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
M = {}
mx, my = 0, 0
with open(fn) as f:
    for y, l in enumerate(f):
        for x, c in enumerate(l.strip()):
            mx, my = max(mx, x), max(my, y)
            M[(x, y)] = Node(x, y, int(c))

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
open_nodes = [M[(0, 0)]]
closed_nodes = []
while open_nodes:
    open_nodes = sorted(open_nodes, reverse=True)
    node = open_nodes.pop()
    closed_nodes.append(node)
    if node == M[(mx, my)]:
        break
    adj = [n for n in node.adj if n not in closed_nodes and n not in open_nodes]
    for n in adj:
        n.gt = node.gt + n.g
    open_nodes.extend(adj)

print('Calculating cost')
print(M[(mx, my)].gt)