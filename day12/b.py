import sys
from collections import deque, defaultdict

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
G = defaultdict(list)
with open(fn) as f:
    for l in f:
        first, second = l.strip().split('-', 1)
        G[first].append(second)
        G[second].append(first)

routes = [] 
to_double = [n for n in G.keys() if n.lower() == n and not n == 'start' and not n == 'end']

print(len(to_double))
i = 0
for double in reversed(to_double):
    i += 1
    print(i, double)
    doubles = [n for n in to_double if n != double]
    doubles.extend(['start', 'end'])
    Q = deque([['start']])
    path = ['start']
    while Q:
        path = Q.popleft()
        if path in routes:
            continue
        if path[-1] == 'end':
            routes.append(path)
            continue
        
        for n in G[path[-1]]:
            if not (n in doubles and n in path):
                if n == double:
                    if path.count(double) < 2:
                        to_check = path.copy()
                        to_check.append(n)
                        Q.append(to_check)
                else:
                    to_check = path.copy()
                    to_check.append(n)
                    Q.append(to_check)
    print(len(routes))
print(len(routes))