
increments = -1
prev = 0
with open('input.txt') as f:
    for l in f:
        if int(l) > prev:
            increments += 1
        prev = int(l)
print(increments)
