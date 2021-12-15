nums = []

with open('input.txt') as f:
    for l in f:
        nums.append(int(l.strip()))

prev = 0
increments = -1
for i in range(2, len(nums)):
    s = nums[i-2] + nums[i-1] + nums[i]
    if s > prev:
        increments += 1
    prev = s

print(increments)
