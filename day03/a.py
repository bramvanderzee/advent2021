
gamma = ''
epsilon = ''
num_ones = [0 for _ in range(12)]
total_lines = 0


with open('input.txt') as f:
    for l in f:
        total_lines += 1
        for i, c in enumerate(l.strip()):
            if c == '0':
                num_ones[i] -= 1
            else:
                num_ones[i] += 1

print(num_ones)
for b in num_ones:
    if b > 0: 
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2),int(epsilon, 2))

print(int(gamma, 2)*int(epsilon, 2))