import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

def generation(fishes: list()) -> list():
    for i in range(len(fishes)):
        f = fishes[i]
        if f == 0:
            fishes.append(8)
            f = 6
        else:
            f -= 1
        fishes[i] = f
    return fishes

fishes = []
with open(fn) as f:
    for l in f:
        fishes.extend([int(n) for n in l.strip().split(',')])

print(fishes)
for i in range(80):
    fishes = generation(fishes)
print(len(fishes))