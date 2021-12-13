import sys
from collections import deque, defaultdict

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
G = defaultdict(list)
with open(fn) as f:
    for l in f:
        first, second = l.strip().split('-', 1)
        G[first].append(second)
        G[second].append(first)

to_double = [n for n in G.keys() if n.lower() == n and not n == 'start' and not n == 'end']

print(len(to_double))
i = 0
routes = defaultdict(list)
for double in reversed(to_double):
    i += 1
    print(i, double)
    Q = deque([['start']])
    path = ['start']
    while Q:
        path = Q.popleft()
        if path in routes[len(path)]:
            continue
        if path[-1] == 'end':
            routes[len(path)].append(path)
            continue
        
        for n in G[path[-1]]:
            if n == double or not (n.lower() == n and n in path):
                if n == double:
                    if path.count(double) < 2:
                        to_check = path.copy()
                        to_check.append(n)
                        Q.append(to_check)
                else:
                    to_check = path.copy()
                    to_check.append(n)
                    Q.append(to_check)
    print(sum([len(v) for v in routes.values()]))
print(sum([len(v) for v in routes.values()]))