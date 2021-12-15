
depth = 0
hor = 0

with open('input.txt') as f:
    for l in f:
        cmd = l.strip().split(' ')
        if cmd[0] == 'forward':
            hor += int(cmd[1])
        if cmd[0] == 'down':
            depth += int(cmd[1])
        if cmd[0] == 'up':
            depth -= int(cmd[1])

print(depth, hor)
print(depth*hor)