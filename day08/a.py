import sys

digits = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abcdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
} # len(d): 2 means '1', 3 means '7', 4 means '4', 7 means '8'

segments = {k:v for v, k in digits.items()}
    
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
lines = []
with open(fn) as f:
    for l in f:
        lines.append(l.strip().split(' | '))

count = 0
for entry in lines:
    out = entry[1].split()
    count += len([n for n in out if len(n) in [2, 3, 4, 7]])
print(count)