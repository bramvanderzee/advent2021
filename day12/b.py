import sys
from collections import deque
from node import Node

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
s_node, e_node = None, None
nodes = {}
with open(fn) as f:
    for l in f:
        first, second = l.strip().split('-', 1)
        if not first in nodes.keys():
            nodes[first] = Node(first)
        if not second in nodes.keys():
            nodes[second] = Node(second)
        
        nodes[first].add_adj(nodes[second])
        nodes[second].add_adj(nodes[first])

routes = [] 
nodes['start'].unique = True
nodes['end'].unique = True
to_double = [n for n in nodes.values() if n.char.lower() == n.char and not n.char == 'start' and not n.char == 'end']
for node in to_double:
    node.unique = True

print(to_double)
print(len(to_double))
i = 0
for double in to_double:
    i += 1
    print(i, double)
    double.unique = False
    Q = deque([[nodes['start']]])
    path = [nodes['start']]
    while Q:
        path = Q.popleft()
        if path in routes:
            continue
        if path[-1].char == 'end':
            routes.append(path)
        
        for n in path[-1].adj:
            if not (n.unique and n in path):
                if n == double:
                    if path.count(double) < 2:
                        to_check = path.copy()
                        to_check.append(n)
                        Q.append(to_check)
                else:
                    to_check = path.copy()
                    to_check.append(n)
                    Q.append(to_check)
    double.unique = True

print(len(routes))