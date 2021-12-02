aim = 0
hor = 0
depth = 0

with open('input.txt') as f:
    for l in f:
        cmd = l.strip().split(' ')
        if cmd[0] == 'down':
            aim += int(cmd[1])
        if cmd[0] == 'up':
            aim -= int(cmd[1])
        if cmd[0] == 'forward':
            n = int(cmd[1])
            hor += n
            depth += aim * n

print(aim, hor, depth)
print(hor*depth)