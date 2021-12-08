import sys

_digits = {
    'cf': 1,
    'acf': 7,
    'bcdf': 4,
    'abcdefg': 8,
    'acdeg': 2,
    'acdfg': 3,
    'abdfg': 5,
    'abcefg': 0,
    'abcdfg': 9,
    'abdefg': 6,
} # len(d): 2 means '1', 3 means '7', 4 means '4', 7 means '8'

segments = {k:v for v, k in _digits.items()}
    
fn = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
lines = []
with open(fn) as f:
    for l in f:
        entry = l.strip().split(' | ')
        entry = (entry[0].split(), entry[1].split())
        lines.append(entry)

# first deduce nums by their length
# we can deduce 'a' if 1 and 7 are both present
def try_decode(entry):
    nums, _ = entry
    len_mapping = { 2: 1, 3: 7, 4: 4, 7: 8 }
    
    digits = {}
    for num in nums:
        if len(num) in [2, 3, 4, 7]:
            digits[len_mapping[len(num)]] = set(sorted(num))
    
    M = {}

    # determine a:
    assert 1 in digits.keys() and 7 in digits.keys()
    M['a'] = list(digits[7] - digits[1])[0]

    # determine e and g: g is always present on len(num) >= 5
    eg = tuple(digits[8] - (digits[4] | digits[7]))
    first, second = eg
    if all([first in num for num in nums if len(num) >= 5]):
        M['g'], M['e'] = first, second
    else:
        M['g'], M['e'] = second, first
    
    # determine b and d: d is always present on len(num) == 5
    bd = tuple(digits[4] - digits[7])
    first, second = bd
    if all([first in num for num in nums if len(num) == 5]):
        M['d'], M['b'] = first, second
    else:
        M['d'], M['b'] = second, first

    # Now we've determined a, b, d, e, g => todo c, f
    # f is the len(5) num if b also in num
    found = set([c for c in M.values()])
    cf = digits[8] - found
    f = [n for n in nums if len(n) == 5 and M['b'] in n]
    assert len(f) == 1
    assert len(set(f[0]) - found) == 1
    M['f'] = list(set(f[0]) - found)[0]
    assert len(cf - set(M['f'])) ==1
    M['c'] = list(cf - set(M['f']))[0]

    mapping = {}
    for k,v in _digits.items():
        out = []
        for c in k:
            out.append(M[c])
        mapping[''.join(sorted(out))] = v

    return mapping

count = 0
for entry in lines:
    mapping = try_decode(entry)
    _, out = entry
    if mapping:
        n = ''
        for num in out:
            n += str(mapping[''.join(sorted(num))])
        count += int(n)
    else:
        print(entry)
print(count)