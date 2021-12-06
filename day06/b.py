import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

nums = []
with open(fn) as f:
    for l in f:
        nums.extend([int(n) for n in l.strip().split(',')])

fishes = {k:nums.count(k) for k in range(9)}
print(fishes)

for i in range(256):
    num_new = fishes[0]
    fishes = {k-1:fishes[k] for k in fishes.keys()}
    fishes.pop(-1)
    fishes[8] = num_new
    fishes[6] += num_new

count = 0
for v in fishes.values():
    count += v
print(count)